```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
        '.': 1,
        'oO': [4, 2],
        'oO|': [2, 2],
        'oo': [2, 4],
        'oo|': [2, 2, 2],
        '.o': [1, 4],
        'OO': [2, 4],
        'ooo': [4, 8],
        '...': -1
    }
    beats = 0
    temp_beat = 1
    notes_used = []
    for note in music_string:
        if note in notes:
            beats += notes[note]
        temp_beat *= notes[note]
        if temp_beat > 1:
            temp_beat = 1
        notes_used.append(beats)
        if note == '...':
            beats = -1
    return notes_used
```