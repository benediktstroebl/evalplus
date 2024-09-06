Here's a self-contained Python function that solves the problem of parsing musical notes represented in a string and returning a list of integers indicating the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    beats = []
    
    for note in music_string.split(' ' '):
        beats.append(notes) = notes.set(notes) for note in notes)
    
    return beats
```
This function uses a dictionary to map the musical note characters to their respective beat values. The function splits the string by spaces and then uses the notes dictionary to map each note to its beat. The beats are then accumulated into a list and returned at the end.