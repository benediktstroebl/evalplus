```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1
    }
    return [notes[note] for note in music_string.get()]
```
This function uses a dictionary `notes` to map the musical note characters to the number of beats they should last.  It string is input is the music_string that is to be parsed.