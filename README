# Dragalia Story Data Parser

This parser scans a directory and its subdirectories for Story MonoBehaviours extracted via AssetStudio as .txt files, and outputs them into a file that formats the dialogues into Dragalia-wiki template friendly formats.

## Usage
1. Run `monoToDb.py` on a directory of parsed game data mono txt files (this builds a sqlite3 db of the game data for straightforwardness of querying.
   * Inspect file internals to edit hardcoded input and output paths (because I'm too lazy to make them arguments).
2. Run `parseStory.py` on a top level directory containing only Story .txt files. 
   * Again, you'll need to edit the hardcoded constants to change the input and output paths, sorry.

Currently the following story types are supported:

### Adventurer
Includes support for both the 5* promotion quote and the regular adventurer stories. Both will output as fields for the [`{{AdventurerStories}}`](https://dragalialost.gamepedia.com/Template:AdventurerStories) template, but not the entire template.

### Dragon
Will output formatted fields for the [`{{DragonStories}}`](https://dragalialost.gamepedia.com/Template:DragonStories) template, but not the entire template.

### Event Quest
Will output entire [`{{EventStoryHeader}}`](https://dragalialost.gamepedia.com/Template:EventStoryHeader) template, filled in with Event details.

### Campaign Quest
Currently unsupported due to lack of example data to test. Will likely try to behave as an Event Quest, but fail horribly.