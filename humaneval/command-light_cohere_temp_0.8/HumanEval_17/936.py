```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    return [notes[char] for char in music_string.

# Example tests
music_str = 'o o| .| o| .| .| o o'
test_parse_music = [
    "Invalid format! Expected 'o', 'o|', '.|', not '.'",
    "Wrong notes format. Expected: 4, 2, 1, not 5",
    "Missing 'o' note.",
    "Got {0}".format(parse_music)
]

for test in test_parse_music:
    assert parse_music(test) == [4, 2, 1], test+" didn't parse correctly"
```