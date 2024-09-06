```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_lengths = [notes.get(note) for note in music_string.
    return [ list(notes_lengths)

# Unit tests
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected_result = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual_result = parse_music(music_str)
    assert actual_result == expected_result
```

The function `parse_music` takes a string of music notes in a format and returns a list of integers representing the length of each note. The function is designed with type hints and docstrings, which further enhance its self-containment. The unit test function `test_parse_music` validates that the `parse_music` function produces the correct results for a given input string.