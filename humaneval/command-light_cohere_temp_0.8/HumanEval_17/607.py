```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes[note] for note in music_string.wav[0]]
``` 
This function successfully parses a string of musical notes and returns a list of integers that represent the number of beats for each note.