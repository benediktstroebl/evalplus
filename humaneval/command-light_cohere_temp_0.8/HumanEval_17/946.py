Here is a Python script with a self-contained function that solves the problem of converting musical notes in a string to a list of integers:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.expect(' ')]
```

This script defines a function `parse_music` that takes a string of music notes as an argument and returns a list of integers. The function uses a type hint `List[int]` to indicate that the return value is a list of integers. The function uses a `notes` dictionary to map musical notes to their respective durations.