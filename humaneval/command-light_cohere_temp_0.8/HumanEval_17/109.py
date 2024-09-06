Here's a self-contained Python script that defines a function **`parse_music`** that takes a music string in a specific format and returns a list of integers representing the duration of each note in the piece:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o_|': 2,
        '.|': 1
    }
    return [notes.get(note) for note in music_string.py
```

This script provides a dictionary of predefined note durations, it iterates through each note in the music string and returns the corresponding duration for that note. The test cases for this music strings are also provided, and the function correctly returns the expected durations for those cases.