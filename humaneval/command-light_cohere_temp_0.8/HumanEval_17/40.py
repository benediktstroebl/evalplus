```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes[x] for x in music_string.
``` 
This code defines a `parse_music` function that takes a music string in a specific format, and returns a list of integers corresponding to the number of beats for each note.