```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes[note] for note in music_string.args
    format = " ".join(beats)
    return [int(x) for x in format.

# Test cases for the parse_music function
print(parse_music('o o| .| o| .| .| .| .| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music('.'))  # Output: []
print(parse_music('oo.'))  # Output: []
print(parse_music('oOo.'))  # Output: [8, 8]
print(parse_music('oooo'))  # Output: []
```