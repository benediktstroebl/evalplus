```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1,
    }
    return [notes[note] for note in music_string.parse(music_string)]

def test_parse_music():
    test_strings = [
        "o o| .| o| .| .| .| .",
        ".",
        "o o o",
        ".",
        "oo",
        "o/o",
    ]
    for test_string in test_strings:
        assert parse_music(test_string) == [4, 2, 1, 2, 1, 1, 1, 4, 4], f"Failed to parse {test_string}"
```
This code defines a `parse_music` function that parses a music string according to a dictionary of note interpretations. The `test_parse_music` function creates a list of test strings and asserts that the `parse_music` function returns the correct result for each test string. 

The `parse_music` function uses the `parse` method to split the music string into a list of notes, and the note interpretations are taken from the `notes` dictionary.