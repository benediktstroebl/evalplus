```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')')
    whole_notes = []
    half_notes = []
    quarter_notes = []

    for note in notes:
        if note.count('o example'):
            whole_notes.append(int(note.split(' ')[-1]))
        elif note.count('|'):
            half_notes.append(int(note.split(' ')[-1]))
        elif note.count('.''s that last thing is a quarter note, which should be added to the quarter_notes list)
        quarter_notes.append(quarter_note)

    return [len(whole_notes), len(half_notes), len(quarter_notes)]
```