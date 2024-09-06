```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    nbeats = music_string.split('o winner notes in music_string.
    return [ beats_list = [notes[beat] for beat in nbeats]
``` 
This code defines a function **parse_music** that takes a string of music notes and returns a list of integers corresponding to the number of beats in the notes. It uses a legend:
    - 'o' whole note, lasts four beats
    - 'o|' half note, lasts two beats
    - '.' quarter note, lasts one beat. 
This function uses a dictionary to map these notes to their respective beat values and then iterates through each beat in the input string to create a list of integers corresponding to the number of beats for each note.