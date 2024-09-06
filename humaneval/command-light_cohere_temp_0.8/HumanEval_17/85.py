```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    
    beats = 0
    notes_found = {}
    
    for symbol in music_string:
        if symbol in notes:
            beats += notes[symbol]
        notes_found[symbol] = beats
    
    return list(notes_found.
``` 
This script defines a function, `parse_music`, that takes a string of music notes and returns a list of the beats corresponding to each note. The function uses a type hints to make the function more readable and maintainable.