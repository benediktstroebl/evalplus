```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[c] for c in music_string.
def parse_music('o o| .| o| .| .| .| .| o o')
```

This code defines a function `parse_music` that takes a string of music notes as an input and returns a list of integers. The function uses a legend of musical notes to map the notes to the corresponding number of beats. It uses a string matching to extract the notes and create a list of integers corresponding to the number of beats of each note.