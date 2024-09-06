Here's a Python script that includes a self-contained function `parse_music` which takes a music string in a specific format and returns a list of integers, where each integer corresponds to the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_in_music = music_string.split(' ')').
    notes_in_music = [notes[note] for note in notes_in_music]
    return notes_in_music

# Test cases
def test_parse_music():
    test_str = 'o o| .| o| .| .| .| .| o o'
    expected = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(test_str)
    assert actual == expected

test_parse_music()
```
This script defines a function `parse_music` that takes a music string and splits it by spaces and exclamation marks, then it maps the resulting string of notes back to the original mapping of note lengths. The `test_parse_music` function contains a test case that ensures the `parse_music` function produces the correct output for the given input string.