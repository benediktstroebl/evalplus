Here is a Python script that includes a self-contained function that solves the problem of parsing musical notes represented as a string in a special format into a list of integers representing the duration of each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    
    result = []
    for note in music_string.replace():
        note = note.translate(notes): notes
        result.append(note)
    return result
```
This function takes a string of music notes represented in a special format, where each character corresponds to a certain duration.

The function uses a dictionary to map the characters to their respective durations, and then loops through the music_string, using the `translate()` method to apply the corresponding mapping. The resulting list contains the the number of beats corresponding to each note.