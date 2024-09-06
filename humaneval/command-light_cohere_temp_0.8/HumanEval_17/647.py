```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
    }
    
    beats = 0
    notes_found = {}
    
    for symbol in music_string:
        if symbol in notes:
            beats += notes[symbol]
        notes_found[symbol] = beats
    
    return list(notes_found.
```