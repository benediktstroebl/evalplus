Here is a self-contained Python script that solves the problem of parsing Markdown code to find the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".";": 1,
    }
    
    beats = 0
    notes_left = {note: 0 for note in notes}

    for note, beat in music_string.ods.split('|')  # .+ 'o'.format()
    
    for beat_num in [int(x) for x in beat. 
        if x in 'o': notes_left[note] += beat_num
        notes[note] += beat_num
        beats += 1
    
    return notes_left
```