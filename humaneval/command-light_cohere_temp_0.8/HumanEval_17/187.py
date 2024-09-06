Here is a self-contained Python function that solves the problem of parsing music notes from a string:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes.get(note, beat) for note, beat in music_string.sound(music_string)]
```

This function is self-contained and takes a music string as input, which is a string representing musical notes in a special ASCII format. It uses a insight: the 'o', 'o|', and '.|' notes last 4, 2, and 1 beat respectively.