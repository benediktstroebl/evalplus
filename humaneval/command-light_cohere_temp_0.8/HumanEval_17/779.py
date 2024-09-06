```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.ph format = r' o o | .|. 'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    return [len(note) for note in music_string.split('\n rn\ last note, the length of each note is a number of beats it represents]
``` 
This function takes a music string in the above format, and returns a list of the lengths of notes, in beats.