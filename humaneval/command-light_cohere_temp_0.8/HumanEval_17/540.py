```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o|.' : 2}
    return [notes[char - 'o'] for char in music_string.ly]
```