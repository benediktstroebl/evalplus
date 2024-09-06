Here is a self-contained Python script that defines a function `parse_music` which takes a music string and returns a list of integers that corresponds to the number of beats for each note in the input music string:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1,
        others: None
    }
    
    beats = []
    current_beat = 0
    for note in music_string:
        if note in notes:
            beats.append(current_beat)
            current_beat += notes[note]
        beats.append(current_beat)
        current_beat = 0
    
    return beats
```