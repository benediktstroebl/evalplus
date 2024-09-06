```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    music_notes = music_string.split(' ' ')
    return [int(note) for note in music_notes if note.isalpha()]
```
This code defines a function **parse_music** that takes a string music_string as input and returns a list of integers. The function splits the string into a list of notes using the split() method and then iterates through the list, converting each note to an integer using the isalpha() method. The resulting list of integers represents the number of beats each note lasted in the input music_string.