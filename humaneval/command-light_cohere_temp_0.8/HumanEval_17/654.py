```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, '/': 4}
    return [notes[ch] for ch in music_string.test_music = "o o|  .|  /|   .|  .|  .|  .| .| o o o"
    assert parse_music(test_music) == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
```
Do you need help with anything else related to coding?