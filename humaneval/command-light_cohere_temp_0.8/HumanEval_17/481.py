```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.example is a str() for note in notes]
```
This code defines a function **`parse_music`** that takes a string of music notes and returns a list of integers that correspond to the number of beats that each note lasts. The function uses a legend where each note can be either a whole note (which lasts 4 beats), a half note (which lasts 2 beats), or a quarter note (which lasts 1 beat). The function then iterates through each character in the string, checking if it is a valid note and looking up its corresponding duration in the legend. The function successfully handles a test cases and provides the expected output for each test.