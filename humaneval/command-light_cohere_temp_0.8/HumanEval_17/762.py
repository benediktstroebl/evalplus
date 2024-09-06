Below is a self-contained Python function that parses a string of musical notes in a special ASCII format and returns a list of integers corresponding to the number of beats of each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = []
    current_beat = 0
    
    for note in music_string:
        if note in notes:
            beats.append(current_beat)
        current_beat += notes[note]
        
    return beats
```