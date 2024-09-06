```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')'). strings = music_string.split(' ')
    problem = []
    for note in notes:
        try:
            if note == 'o':
                beat = 4
            elif note == 'o|':
                beat = 2
            elif note == '|':
                beat = 1
            else:
                raise ValueError("Invalid note! ")
            problem.append(beat)
        if note == '>'
            return problem
    return [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
```