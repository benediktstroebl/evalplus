```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
    }
    return [notes[note] for note in music_string.test_music_parse(music_string)]

# Example test cases
test_music_parse = parse_music('o o| .| o| .| .| .| o o')
test_music_parse(' ')
test_music_parse('o o o| .')
test_music_parse('Too many notes')
```
This script defines a function `parse_music` that parses a music string in the Markdown code format and returns a list of integers that represent the number of beats for each note. The function uses a legend:
- 'o': whole note, lasts four beats.
- 'o': half note, lasts two beats.
- '.|': quarter note, lasts one beat. 

The function uses a dictionary `notes` to map these legend characters to the respective beat values. 

Please note that this is a self-contained solution, and it does not require any external modules or functions.