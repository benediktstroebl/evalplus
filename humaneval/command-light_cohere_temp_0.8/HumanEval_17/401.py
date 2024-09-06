```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    return [notes[ch] for ch in music_string.get()]
```
This function parses a string representing musical notes in a special ASCII format, and returns a list of integers corresponding to how many beats does each note last.