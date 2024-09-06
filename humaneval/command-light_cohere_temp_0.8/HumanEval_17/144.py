```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}  # map of music notes and their beats
    beats = music_string.split(' ') '  # split string into lines
    lines = [line.split(' o|') for line in beats]
    output = []
    for line in lines:
        temp = [notes[note] for note in line]
        output.append(temp)  # convert list of notes into list of beats
    return output
```