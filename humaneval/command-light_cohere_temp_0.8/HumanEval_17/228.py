```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[c] for c in music_string.or music_string]
 [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This code defines a function, `parse_music`, that takes a string of music notes, then converts that string into a list of integers representing the duration of each note in beats. The function uses a legend of notes, which are mapped to the integer values representing the duration of a whole note (`4`), a half note (`2`), and a quarter note (`1`).  The function then returns this list.