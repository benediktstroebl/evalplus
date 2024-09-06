```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beats = music_string.split(' ')
    time: [beat.split('|')]
    }. The time is a beatlist, each time:
    if beat[-1] == 'o':
        beat[-2:] = notes[beat[-1]]
    else:
        beat[-2:] = 1
    return [beat[:-len(beat) // 2] for beat in time]
```