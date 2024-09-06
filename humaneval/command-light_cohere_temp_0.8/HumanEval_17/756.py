Here's the Python script that includes a self-contained function `parse_music` that takes a music string in the format and returns a list of integers representing the number of beats for each note:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        other: 0
    }
    return [notes[note] for note in music_string.split(' '|')]
```

This script provides a dictionary `notes` that maps the musical note characters to their respective beat values. It splits the other string into individual notes and then loops through each note, converting it to its corresponding beat value.