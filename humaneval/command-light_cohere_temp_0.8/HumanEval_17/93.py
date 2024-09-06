Here's the solution:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    beats = music_string.split(' '|')
   
    notes_list = []
    for beat in beats:
        note = beat.split('o gem = beat.split('.')[0]
        gem_code = int(gem)
        notes_list.append(notes[notes[note])
    return notes_list
```

This function takes a string of music notes represented in the special ASCII format and returns a list of integers corresponding to the number of beats in each note.