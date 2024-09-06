Here's a self-contained Python function that parses a string of musical notes represented in a specific format and returns a list of corresponding beat counts:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    beats = [notes[note] for note in music_string.split(' '|')]
    return beats
```
This function takes a string music_string as input and uses a dictionary to map musical notes to their respective beat counts. The function splits the string by '|' characters and uses a list comprehension to extract the beat counts corresponding to each note. The beats are then converted into a list of integers representing the number of beats for each note.