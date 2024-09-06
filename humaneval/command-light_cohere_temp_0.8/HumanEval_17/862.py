Here's a Python script with a self-contained function that solves the problem of parsing and matching musical notes in a string:
```python
from typing import List
from collections import defaultdict

NOTES = {'.o' - whole note, lasts 4 beats', 'o| - half note, lasts 2 beats', '.| - quarter note, lasts 1 beat'}

def parse_music(music_string: str) -> List[int]:
    notes = defaultdict(int)
    for note in NOTES:
        notes[note] = music_string.find(note, 4)
    return notes.
``` 
The function uses a defaultdict to store notes and counts their occurrences in the music string.