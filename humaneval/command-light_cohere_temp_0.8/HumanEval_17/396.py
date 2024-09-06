Here's the self-contained Python function:
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 4,
        "O": 4,
        "oO": 8,
        "oooo": 4,
    }
    
    beats = [notes.get(note, beat) for note in music_string.strip(). note_counts = [0]
    for note in music_string:
        note_counts += [beats.get(note, 0)] * int(note.re.note.append(note_counts)
    
    return note_counts


```

This function will parse the given string representing musical notes in a special ASCII format and return the number of beats corresponding to how many beats each note lasted.