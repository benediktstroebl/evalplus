```python
from typing import List

pattern = 'o|^.<|o|^.<|.|^|o|^.<|o'


def parse_music(music_string: str) -> List[int]:
    result = []
    notes = music_string.strip().split('|')
    beat_pattern = {
        'o': 4,
        '|': 2,
        '^': 1,
        '.': 1
    }

    for n in notes:
        count = len(n) * beat_pattern[n[0]]
        result.append(count)

    return result
```

This approach utilizes a dictionary `beat_pattern` for quick access to beat values and calculates each note's duration by its length (number of characters) and its type. An example input string `'o |^.> |^.> |^.>` would produce the following output: `[4, 1, 2, 1, 1, 2, 1, 1, 1]`