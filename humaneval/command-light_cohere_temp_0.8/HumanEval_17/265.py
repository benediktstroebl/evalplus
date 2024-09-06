Here's a Python script that defines a function `parse_music` to parse a given music string representing musical notes in a special ASCII format, and returns a list of integers corresponding to the duration of each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        others: []
    }
    
    beats = []
    for note in music_string.split(" " ")[::-1]:
        if note in notes:
            beats.append(notes notes[note])
        else:
            beats.append(4)  # Add a whole note to beats list
    
    return beats
```