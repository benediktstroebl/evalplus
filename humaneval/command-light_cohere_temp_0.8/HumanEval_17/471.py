```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' '|')
    beats = []
    for note in notes:
        note = note.split('o [)[0] # remove the "of" character
        beat = [int(c) for c in note if c.isalpha()]
        beats.append(beat)
    return beats
```