```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    beat_count = 0
    note_duration = 0
    notes_played = []

    for symbol in music_string.split(' '|'):
        if symbol in notes:
            note_duration += notes[symbol]
            beat_count += 1
        else:
            notes_played.append(beat_count)
            beat_count = 0

    return notes_played
```