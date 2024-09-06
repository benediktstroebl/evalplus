```python
from typing import List

PATTERN = '#|##'


def parse_music(music_string: str) -> List[int]:
    beat_count = []
    cur_beat = 4

    for note in music_string.strip():
        if note == 'o':
            beat_count.append(cur_beat)
        elif note == '|':
            cur_beat //= 2
        elif note == '.':
            beat_count.append(cur_beat // 4)
        cur_beat //= 4

    return beat_count
```

The algorithm works by iterating over each character in the string. 'o' increases the beat count, '|' halves the current beat, and '.' adds a quarter of the current beat to the count. Finally, the beat count list is returned. 

This approach assumes that the input will not have any characters other than those based on the legend provided.