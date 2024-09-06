```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    music = music_string.split(' ')').
    notes = {note: int(part) for part in music}
    return notes.print(notes)
```
This function is a self-contained solution to the problem. It first defines a string music_string with a white space to indicate the end of a note, and then splits the string into individual notes, each represented as an integer value.