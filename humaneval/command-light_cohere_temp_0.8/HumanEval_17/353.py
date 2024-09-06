```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = [notes[symbol] for symbol in music_string if symbol in notes]
    return notes_list
```