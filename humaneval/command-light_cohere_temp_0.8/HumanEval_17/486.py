```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    notes_length = [notes.get(x, beat) for (beat in music_string.return]
    code_ ... 
    return notes_length
```