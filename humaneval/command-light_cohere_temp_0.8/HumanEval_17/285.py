```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beat = 1
    result = []
    for note in music_string.split(' ' '):
        if note in notes:
            count = int(note[0])
            result.append(beat * count)
            beat += 4
        else:
            result.append(beat * int(note))
            beat += 1
    return result
```