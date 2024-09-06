Here's a self-contained Python function that takes a string of music notes in a special ASCII format and returns a list of integers, each corresponding to how many beats does each note last:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' | '|')
    beats = []
    for note in notes:
        note = note.split('o region')
        times = [int(x) for x in note]
        beats.append(times)
    return beats
```
This function splits the input string into a list of notes, then splits each note into a list of regions (representing different beat lengths), and finally converts that list of regions into a list of beat values.