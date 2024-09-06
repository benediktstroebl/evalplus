```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    pattern = r'([02468]|.){rs'
    return [int(c) for c in pattern.match(music_string). note_str(notes)]

# Test case 1
test_music1 = 'o o| .| o| .| .| o o' o o' '
assert parse_music(test_music1) == [4, 2, 1, 2, 1, 2, 1, 1, 1, 4, 4]

# Test case 2
test_music2 = 'o o| .| .| .| o o' '
assert parse_music(test_music2) == [1, 1, 1, 1]

# Test case 3
test_music3 = '..| .'o|..'
assert parse_music(test_music3) == []
```