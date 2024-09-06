```python
from typing import List

PATTERN = {'o': 4, 'o|': 2, '.|': 1}


def parse_music(music_string: str) -> List[int]:
    result: List[int] = []
    curr_beat = 0
    for c in music_string:
        if c in 'o|.|':
            curr_beat += PATTERN[c]
        else:
            result.append(curr_beat)
            curr_beat = 0
    result.append(curr_beat)
    return result
```

The `parse_music` function takes a string input and iterates over each character. It accumulates the length of each note and adds the total to the result list. Lastly, it returns the list of beats corresponding to each note.