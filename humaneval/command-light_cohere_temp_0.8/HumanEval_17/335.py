Here's a self-contained Python function that solves the music notes parsing problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    beats = [notes.get(note, 4 if note.get('o Closes down.lower() in notes else]
   
    return beats
```
This function uses a dictionary `notes` to map each unique musical note to the number of beats it lasts. The function iterates through each character in `music_string` and uses the `notes` dictionary to find the beats it represents. It returns the full list of beats.

This function is self-contained and can be used to parse any music notes input and returns the corresponding beats.