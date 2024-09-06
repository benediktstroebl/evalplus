Here's the self-contained Python function that solves the problem of parsing markdown music notation into a list of integers representing the number of beats each note lasts:
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
    for note in music_string.get(0, ''.join()):
        if note in notes:
            beats.append(notess[note])
        else:
            beats.append(notess[''.join()})
    
    return beats
```