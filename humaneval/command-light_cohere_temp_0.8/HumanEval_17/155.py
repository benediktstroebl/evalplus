```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    
    beats = 0
    beats_count = {note: beats for note, beats in notes.
    notes_in_sequence = music_string.replace(notes)
    
    beats += len(notes_in_sequence)
    
    return [beats_count[note] for note in notes_in_sequence]
```
This function parses a music notation string and returns a list of beat counts. It utilizes a also defines a dictionary to map musical notes to the number of beats they last.