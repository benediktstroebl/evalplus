```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[c] for c in music_string.sample]
```

# Test
music_str = 'o o| .| o| .| .| .| .| o o'
assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]