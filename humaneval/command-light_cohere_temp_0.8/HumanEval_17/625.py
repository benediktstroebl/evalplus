Here's the self-contained Python function to solve the problem of parsing Markdown music code and returning the number of beats corresponding to each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        "o|.":": 2,
        "|.":": 1,
        }.from
    }
    
    beats = []
    current_beat = 0
    for note, beat in notes.
    note_ends_with_newline = False
    
    for char in music_string:
        if char == "\n":
            if not_ends_with_newline:
                beats.append(current_beat)
            current_beat = 0
            not_ends_with_newline = True
        elif char in "|.":":
            current_beat += beat
            not_ends_with_newline = True
        elif not_ends_with_newline:
            not_ends_with_newline = False
        else:
            current_beat += 1
    
    return beats
```