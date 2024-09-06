Here's a Python script that defines a function parse_music that takes a music string and returns a list of integers:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        ".":o|": 2,
        "....": 4
    }
    return [notes.get(note, beats) for note, beats in music_string.stri(note, 'o']
```
This function utilizes a dictionary to map musical notes to the number of beats they represent. It then iterates through this string and returns the corresponding integer values.