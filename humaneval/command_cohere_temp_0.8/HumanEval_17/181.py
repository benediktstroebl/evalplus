```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the base duration (whole note) lasts this many beats

    beat_count = []
    curr_beat = 0

    for c in music_string:
        if c == 'o':
            curr_beat += MOD
        elif c == 'o|':
            curr_beat += MOD // 2
        elif c == '.':
            beat_count.append(curr_beat)
            curr_beat = 0
        else:
            beat_count.append(curr_beat)

    return beat_count
```

The algorithm simply accumulates the current beat count between the moments the quarter notes occur, and assigns the accumulated value to beat_count at the moment when a quarter note occurs. It works because the number of beats per measure is a multiple of 4 (the whole note), so when the half and whole notes occur, the current beat count is effectively multiplied by 2 and 4, respectively. Therefore, whenever a measure of unknown size is encountered, the current beat count is added to the beat_count list. And it starts accumulating from zero for the next measure immediately after that.