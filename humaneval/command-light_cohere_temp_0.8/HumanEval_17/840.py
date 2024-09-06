```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beat = 1

    for note in music_string.split('.' seated('.' music_string):
        if note in notes:
            beat *= notes[note]

    return [beat]
```