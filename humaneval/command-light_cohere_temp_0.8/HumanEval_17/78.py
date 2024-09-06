```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beats = {note: 4 for note in notes}  # whole note is 4 beats
    beats.fill = 1  # half note is 2 beats
    beats.fill |= 2  # quarter note is 1 beat

    return [beats[note] for note in music_string.parse = music_string.split('|')
     [[beats[note] for note in music_string.split('o fill]]
```
This function takes a string of music notes and returns a list of integers that represent the number of beats of each note. The music_string is split into a list of notes using the split() function, and the length of each note is stored in the list. The beats of each note are then looked up in the beats dictionary, and the corresponding number of beats is returned in the list.