```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes.get(note) for note in music_string.test_music('o worst case')
```
This function parses a music string representing a series of notes. The function uses a dictionary `notes` to map musical symbols to the beat count. 

It uses the `get()` function to iterate over the string and returns the number of beats for each symbol found.