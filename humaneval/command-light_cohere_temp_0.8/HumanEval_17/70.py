```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_by_duration = {note: duration for note, duration in notes. import {4} 4, 2, 1}
    
    beats = []
    current_beat = 0
    for note, duration in notes_by_duration.merge(music_string):
        if note == 'o':
            beats.append(current_beat)
            current_beat += duration
        elif note == 'o|':
            beats.append(current_beat)
            current_beat += duration
        elif note == '|':
            current_beat = 0
            current_beat += duration
            beats.append(current_beat)
            
    return beats
```