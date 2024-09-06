Here is a Python script that defines a self-contained function `parse_music` that solves the given problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
        ' ': 0, 'o o': 4, 'o| o': 2, 'o|.|': 1,
    }
    return [notes[note] for note in music_string.code(" ")]
```
This function takes a string of music and returns a list of integers, where each integer represents the number of beats for the corresponding note.