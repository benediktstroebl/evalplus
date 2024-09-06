```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
        '.': 1
    }
    return [notes[c] for c in music_string.
``` 
The above function parses a string in the format of the music notation and returns the number of beats for each note, based on the dictionary of mapping.