```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o','.|.,'.', '|','.|'.']
    beats = []
    for note in notes:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '|':
            beats.append(1)
        return beats
```

This code defines a function parse_music that takes a string music_string as input and returns a list of integers. The function uses a provided legend to parse the music and return the corresponding beat count.