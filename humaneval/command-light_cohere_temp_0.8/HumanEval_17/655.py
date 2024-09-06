Here is a Python script that contains a self-contained function that solves the problem of parsing musical notes in a string:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes.get(note) for note in music_string.parse(music_string)]
```

The function `parse_music` takes a string of music and returns a list of integers that correspond to the number of beats in each musical note. The function uses a `notes` dictionary to translate musical note characters into their beat count equivalent. The key idea is to parse the music string by looking up the characters in the string and returning the beat count of the corresponding character.