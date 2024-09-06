```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = []
    music = music_string.split(' ')')
    important = [0]*len(music)
    current_beat = 0
    for note in music:
        if note in notes:
            beats.append(important[current_beat])
            current_beat += notes[note]
        else:
            beats.append(important[current_beat])
            current_beat = 0
    return beats
```