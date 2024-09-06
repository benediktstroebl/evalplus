```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o','.', '|','.', '.']
    pattern = r'(?:? plain(\d whole| halt)'
    beat = 4
    start = 0
    for note in music_string.split(' '.' .')[::-1]:
        if note not in notes:
            raise ValueError(f'Invalid note: {note}. Must be one of: {notes}')
        if note == 'o':
            start += beat
        elif note == 'o|':
            start += beat // 2
        elif note == '|':
            start += beat // 4
        else:
            raise ValueError(f'Invalid note: {note}. Must be one of: {notes}')
        if start < 0:
            raise ValueError('Please input the notes in order of whole, half, quarter')
        beat -= start
        yield beat
    return [x for x in beat]
```