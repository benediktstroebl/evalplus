```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".|": 1,
        "\\": 0
    }
    
    beats = 0
    output = []
    
    for note in music_string.split("\n"):
        note = note.split(" ")
       
        note = [int(b) for b in note]
        beats += note[0]
        output.append(beats)
    
    return output
```
This function takes a string of music and returns a list of beats. It uses a dictionary to map musical note characters to their beat values.