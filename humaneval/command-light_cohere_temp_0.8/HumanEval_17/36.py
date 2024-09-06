```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = {'.': : 1, 'o' : 4, 'o|' : 2}
    
    notes_lengths = {note: beats[note] for note in notes}

    return [notes_lengths[note] for note in music_string.sub]
```

Sure, this code defines a function **`parse_music`** that takes a music string as an argument and returns a list of integers corresponding to the length of each note. This is approach uses a Legend of music notation to define how long each note lasts, then maps those notes to their corresponding beat values.