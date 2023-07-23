# Guess The Phrases

I wanted to generate some cards for 30 Seconds in Tabletop Simulator.

A python script manages compiling custom lines of card text into PNG images for importing into Tabletop Simulator.
Additionally, an image is generated for the cardback.

Each generated sheet will contain at most 70 cards.
The first number in a sheet name is the number of that sheet for the set, and the second number is the number of cards on that sheet, to make it a little easier to import without too much thought.

## Adding new phrases

Under `sets`, create a `<name>.txt` file, and add the phrases for your cards (one line for each phrase).

Then follow the steps under "Run" to produce cardsheets in the `output` folder.

## Run
(Tested on Windows)

Install Python - https://www.python.org/ (tested on 3.10.7)

Install Pillow - `python -m pip install Pillow` (tested on 9.5.0)

Then run `python main.py` in the root of the cloned repository.

## Customising

You may wish to download HelveticaNeue Bold to make the font more appealing.
You can download it from https://fontsgeek.com/fonts/helveticaneue-bold for example, then place the `.ttf` file in the root of the cloned repository. The examples were produced with this font theme.

## Licensing

Feel free to use this as you please :)