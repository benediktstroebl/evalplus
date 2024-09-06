```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    pattern = r'[\d]+'o|\]|\d+'
    notes_list = re.compile(pattern, music_string).
    return [notes[notes_list]
```