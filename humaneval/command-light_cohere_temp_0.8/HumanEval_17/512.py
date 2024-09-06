```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o|.' : 4}
    return [notes[ord(char) - 96] for char in music_string.

# Test cases
print(parse_music('o o| .| o| o| .| .| .| .| o o')) # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music('.')) # Output: []
print(parse_music('oo')) # Should return []
print(parse_music('o o o')) # Should return [4, 4]
print(parse_music(' foo')) # Should return []
```