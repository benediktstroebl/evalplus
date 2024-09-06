```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_nums = {note: notes[note] for note in music_string.
    
    return [list(map(notes_num, music_string.from() -> 0))
```
This code defines a function **`parse_music`** which takes a string music_string as input. It uses a string mapping to map each music note to its corresponding number of beats. The code then maps the list of integers to return, which are the number of beats for each note in the string.