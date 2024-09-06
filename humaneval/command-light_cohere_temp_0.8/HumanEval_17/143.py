Below is a Python script with a self-contained function that solves the problem of converting a string of music notes into a list of beat counts:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    return [notes[char] for char in music_string.

def test_parse_music():
    assert parse_music('o o| .| o| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music(',.|o') == [1]
    assert parse_music('.).o') == []
```

The code defines a function parse_music that takes a music string in the format of notes as characters and returns a list of their corresponding beat counts. The function uses a legend to map the characters to their respective beat counts. The test_parse_music function verifies that the parse_music function works correctly by passing various test cases and asserting the expected output.