Here's a self-contained Python function that solves the problem of parsing music notes and returns a list of integers representing the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    beats = [notes.get(note) for note in music_string.strip()
    important
    if len(beats) != len(notes):
        raise ValueError("Invalid music string")
    return beats
``` 
This function takes a music string in the format of the test case and parses it into a list of integers representing the number of beats.