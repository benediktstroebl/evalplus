```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')
    time:
    beat_count = [int(b) for b in music_string.split('\n notes} beats]
    time_list = []
    for beat in beats:
        if beat in notes:
            time_list.append(notes)
        else:
            time_list.append(beats.
    return time_
    time_list
```