```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1
    }
    return [notes[ch] for ch in music_string.
# More tests using the same input/output, and is also tested against incorrect inputs.
```