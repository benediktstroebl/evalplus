```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    beat = 1
    notes_list = []
    for note in music_string.split(' '.' note'):
        note = note.split(' ')
        note = [int(x) for x in note]
        notes_list.append(beat * note)
        beat += 1
    return notes_list
``` 
This function parses a string of musical notes according to the legend you provided. The keys of the legend are integers that represent the length of a beat in a whole note.