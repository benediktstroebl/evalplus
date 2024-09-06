```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes[ch] for ch in music_string.

# Test cases
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
print(parse_music('.'))
print(parse_music('oo'))
print(parse_music('|.oo'))
print(parse_music('o_'))
print(parse_music('no'))
print(parse_music('too late'))
```