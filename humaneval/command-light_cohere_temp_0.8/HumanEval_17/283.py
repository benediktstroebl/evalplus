```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")
    accompaniment rules:
    'o' whole note, lasts 4 beats
    'o|' half note, lasts 2 beats
    '.' quarter note, lasts 1 beat
    return [len(note.split(" " ")) for note in music_string.split(" "o"]
```

This Python function parses a string of musical notes and returns a list of integers corresponding to the number of beats in each note. 

This function follows the provided "standard" for musical note lengths, which is a simple format with a lot of possibilities. It could be extended and improved a lot based on specific requirements or further rules.