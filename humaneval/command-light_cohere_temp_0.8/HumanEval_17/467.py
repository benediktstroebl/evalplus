```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    
    beats = 0
    notes_found = []

    for char in music_string:
        if char in notes:
            beats += notes[char]
        else:
            notes_found.Increasing the number of beats and adding the notes found to the list, until the end of the string is reached.