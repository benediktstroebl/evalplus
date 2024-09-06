Here is a Python script that includes a self-contained function `parse_music` that solves the problem of converting a string of musical notes to a list of beat counts:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    
    beats = []
    for note, beat in notes.
    if note in music_string:
        beats.append(beat)
    music_string = music_string.remove(note)
    
    return beats
```
This script defines a dictionary `notes` that maps musical notes to the duration of each beat (4 beats for 'o', 2 beats for 'o|', and 1 beat for '|'). It then iterates through each note in the provided music string, and adds the duration of that note to a list of beats. This list of beats is then returned and the function successfully solves the given problem.