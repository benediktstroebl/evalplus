Here's a self-contained Python function that takes a string of music notes in a special ASCII format, and returns a list of integers corresponding to the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1,
    }
    
    beats = [notes.get(x, 0) for x in music_string.strip_note]
   
    beats.append(notes.get('.first_note_rest, 0) for first_note, last_note in music_string.filter(first_note != last_note))
    
    return beats
``` 
This function uses a dictionary to map the music notes to the number of beats each note takes. It iterates through `notes` until the note is the last one in the string.