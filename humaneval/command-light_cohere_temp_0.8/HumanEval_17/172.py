```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        ".";": 1,
    }
    return [notes[note] for note in music_string.

# Test the function
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
 ```