```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')
    importants only in music_string.
    return [length(beats) // return the number of beats, not the actual beat
    beats = [notes.get(note) for note in beats]
    return beats
```