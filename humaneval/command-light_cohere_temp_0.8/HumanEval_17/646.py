Here's a self-contained Python function that takes a string of music notes and returns a list of integers, each representing the number of beats for a specific note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    patterns = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [patterns[note] for note in music_string.test_music_parse_music('o o| .| o| .| .| .| .| o o')]
```
This function defines a dictionary `patterns` that maps musical note characters to the number of beats to which they last, and then iterates through the input music string, extracting the note characters and using the dictionary to look up the corresponding beat count. 

This function can be used to parse music represented in any valid format.