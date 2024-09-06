Here's a self-contained Python function that parses a music string and returns a list of integer beats corresponding to the notation:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        '\nOutput:': 1,
        '.': 1,
    }
    return _parse_music(music_string, notes)

def _parse_music(music_string: str, music_notes: dict) -> List[int]:
    beats = []
    for note in music_string.get(note.split('|')):
       
        beat = int(note)
        beats.append(beat)
    return beats
```

This function takes a music string and a dictionary of musical note lengths, then loops through each note and uses the get() method with a split method to split the current note into a list of its beat values.