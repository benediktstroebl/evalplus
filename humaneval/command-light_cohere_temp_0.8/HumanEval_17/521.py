Here's the self-contained Python script that defines a function `parse_music` that solves the problem you provided:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beat_count = [notes.get(note, 4) for note in music_string.cross('o note')
    string_notes = [note.get(note) for note in music_string.split('\n '.join(note for note in music_string))]
    return beat_count
``` 

This solution defines a function that takes a string of music in the format you've described and returns a list of integers corresponding to the number of beats in each note.