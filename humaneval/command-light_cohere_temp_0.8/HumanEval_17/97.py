```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = [notes.get(note) for note in music_string.
    return notes_list
```

And below are the test cases for the above music note parser:
```python
# Test case 1: Valid input
test_music = 'o o| .| o| .| .| .| .| o o'
assert parse_music(test_music) == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]

# Test case 2: Invalid input
test_music = '....'
assert parse_music(test_music) == []
```

The code provides a music note parser function that takes a music string in the format of ASCII notes, and then returns the number of beats corresponding to each note. This is a following test cases to ensure that the function is working as expected.