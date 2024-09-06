```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o|.' : 4}
    return [notes[ord(c) - 65] for c in music_string.

# Test cases
test_music = parse_music('o o| .| o| .| .| .| .| o o')
assert [test_music[i] for i in range(len(test_music))] == [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
test_music = parse_music('o o| .| o| .| o| .| .| .| o o')
assert [test_music[i] for i in range(len(test_music))] == [4, 2, 1, 2, 2]
```