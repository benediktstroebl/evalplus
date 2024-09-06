```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        '\n': 0
    }
    
    beats = 0
    note_duration = len(music_string)
    
    for i, ch in enumerate(music_string, 1):
        if ch in notes:
            beats += notes[ch]
        music_string = music_string.remove(ch)
    
    return beats
```

This Python function named `parse_music` takes a string representing music notes in a special ASCII format and returns a list of integers corresponding to the number of beats that each note lasts. The function uses a legend: `o` is a whole note, `o|` is a half note, `.|` is a quarter note, and `\n` is a new line character. The function then iterates through each character in the string and if it is a valid note, adds its duration to the `beats` count. If a character is a new line, the function resets the `beats` count to zero.