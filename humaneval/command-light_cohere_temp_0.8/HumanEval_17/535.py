```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4, "o|": 2, "|.":": 1,
    }
    return [notes[ch] for ch in music_string.

# Test cases
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
# Should print [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
print(parse_music(''.join'))
# Should print []
print(parse_music(' '.join'))
# Should print []
print(parse_music('Yep!'))
# Should print []
```