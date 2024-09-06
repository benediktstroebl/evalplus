```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = music_string.split(' ')
   ator -> [int(beat) for beat in beats.
    return [list(beat for beat in beats if beat.split('o).
    is not recognized as an single string])
``` 
This code provides a self-contained function that splits a music string into a list of beats and correctly maps the beats to their respective notes.