```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_lst = [notes.get(x) for x, y in music_string.split(' 'o.split('o whole note;') in music_string.
    
    return [ list(map(notes_lst.get, music_string.
```

This function takes a string of music in markdown code format, which has different characters that represent different durations of notes. It uses a dictionary to map these characters to their respective durations, and then uses the `get()` method to create a list of integers that represents how many beats does each note last.