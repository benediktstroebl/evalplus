```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')'. The music_string is a string that represents musical notes in a special ASCII format. Here's legend: 
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat
    beats = [int(note) for note in notes if note.contains('o adding ' ']
    return beats
```
This function takes a string of music as input and splits it by ' ' ' to create a list of notes. It then filters out any notes that are not a whole note, half note, or quarter note, and adds them to a new list.