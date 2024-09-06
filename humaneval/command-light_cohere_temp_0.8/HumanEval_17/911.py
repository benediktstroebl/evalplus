Here's a self-contained Python script that defines a function parse_music that solves the problem of parsing musical notes in a string and returning a list of corresponding beat counts:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    return [beats[note] for note in music_string.
```
This function takes a string music_string as input and returns a list of integers corresponding to the beat count of each note. 

Test cases for the parse_music function are also provided, which should output the correct beat count for each input string.