from pathlib import Path
from random import seed, shuffle
from typing import Iterator


from cardsheet import Colour, batch, create_cardsheet

OUTPUT_DIR = Path("output")
SETS_DIR = Path("sets")

TITLE = "Guess The Phrases"

PHRASES_PER_CARD = 5


def main():
    seed(0)
    OUTPUT_DIR.mkdir(exist_ok=True)

    create_cardsheet(
        OUTPUT_DIR / "back.png",
        Colour.CADMIUM_YELLOW,
        Colour.BLACK,
        [TITLE],
        rows=1,
        columns=1,
        margin=0,
        font_size=120,
        text_gap=60,
    )

    categories = list(_read_categories())
    cards = _shuffle_evenly(categories)
    for i, card_batch in enumerate(batch(list(cards), 70)):
        name = OUTPUT_DIR / f"batch_{i}_{len(card_batch)}.png"
        create_cardsheet(name, Colour.CADMIUM_YELLOW, Colour.BLACK, card_batch, font_size=48)


def _read_categories() -> Iterator[list[str]]:
    for cat in SETS_DIR.iterdir():
        yield [_clean(word) for word in cat.read_text(encoding="utf-8").splitlines()]


def _clean(word: str) -> str:
    return word.split("(")[0].strip()


def _shuffle_evenly(categories: list[list[str]]) -> Iterator[str]:
    for cat in categories:
        shuffle(cat)
    while sum(bool(cat) for cat in categories) >= PHRASES_PER_CARD:
        for i in reversed(range(len(categories))):
            if not categories[i]:
                del categories[i]
        shuffle(categories)
        yield "\n".join(cat.pop() for cat in categories[:5])


if __name__ == "__main__":
    main()
