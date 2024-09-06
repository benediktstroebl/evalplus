Here's the self-contained Python function that parses markdown music code and returns a list of integers representing the number of beats for each note:
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
    for note in music_string.split(' ' '):
        if note in notes:
            beats.append(current_beat)
            current_beat += notes[note]
        else:
            beats.append(0)  # Added for cases where we encounter a new note.
    return beats
```
This function utilizes a dictionary `notes` to map musical notes to the number of beats each note lasts. It then iterates through each character in the input string. Once a input string is split into individual notes using the `split()` method, the function checks if each note is in the `notes` dictionary. If it is, the number of beats is added to the `beats` list, and the current beat count is updated with the value from the dictionary. If it's not a notes, a placeholder value of 0 is added to the `beats` list.