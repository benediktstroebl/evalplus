```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        "..": 4,
        "oO": [4, 4],  # Test: Matches the half note with two beats
    }
    return [notes.get(note, beats) for note, beats in music_string.toLowerCase(music_string.split("\n") if note != ""]
```
This Python function, `parse_music`, takes a string of music notes as input and returns a list of integers. The function uses a dictionary `notes` to map musical notes to the number of beats each lasts. The function splits the string into individual notes, then uses the `get` method to get the beats for each note, and returns the list of beats.