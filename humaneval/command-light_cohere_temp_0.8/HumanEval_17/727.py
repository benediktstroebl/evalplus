```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
        '\n': 0, '\t': 0, ' ': 0, '-': 1, 'oO': 4, 'oO|': 2, 'oO.':: 1,
    }
    return [notes.get(char, beat) for char in music_string.parse()];
```