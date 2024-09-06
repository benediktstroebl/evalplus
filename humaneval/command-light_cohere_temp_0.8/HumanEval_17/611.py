```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    
    beats = [notes[note] for note in music_string.split(' '|')]
    
    return beats
```