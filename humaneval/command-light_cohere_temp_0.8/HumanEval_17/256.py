Here is a self-contained Python function that parses a music string and returns a list of integers representing the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, '/': 4}
    return [notes[char] for char in music_string.
```
The function parses the music_string and returns a list of integers corresponding to the number of beats for each note.