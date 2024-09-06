```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes[note] for note in music_string.beat

    return [beats
```
The above code defines a function named `parse_music` that takes a string music_string as input. The string is parsed into a list of integers corresponding to the number of beats for each note.