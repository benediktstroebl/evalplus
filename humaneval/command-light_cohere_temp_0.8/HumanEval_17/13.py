```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')')
    Some notes, beats and beats[-1] = beats[0] + beats[-1]
    return [int(beat) for beat in beats]

# Test the function with several inputs
assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
assert parse_music('o o o o| .| .| .') == [8, 4, 4, 4]
assert parse_music(' ') == []
assert parse_music(''.split('.') == [0])
```
This script defines a function `parse_music` that takes a music string as input and returns a list of integers. The music string is split into individual notes and beats, and the function maps the beats back to the corresponding note values. The test section ensures the test the function with various inputs.