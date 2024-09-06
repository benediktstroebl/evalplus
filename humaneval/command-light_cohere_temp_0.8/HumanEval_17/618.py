Below is a self-contained Python function that parses markdown music code into a list of integers representing the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 
        'o|' : 2,
        '.|' : 1,
        '\'' : 0,
        other : None
    }
    
    beats = 0
    notes_found = {}

    for note in music_string:
        if note in notes:
            beats += notes[note]
        notes_found[note] = beats

    return notes_found
```
This function will return a dictionary containing the number of beats for each unique note found in the music string.