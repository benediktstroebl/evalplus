```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' | 'o' + '). It's important to split the string based on the '|', assuming that's the separator to define a new note.
 notes = [int(note) for note in notes]
    return notes

def test_music():
    music_string = "o o| .| o| .| .| .| .| o o"
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(music_string)
    assert expected == actual, f"ERROR: {expected} != {actual}"

# You can use test_music() to run the tests
```

The function `parse_music` parses the string of musical notes, and the `test_music` function tests the `parse_music` function with a given string of music. The test compares the expected notes length and rhythm with the actual notes returned by the function, and verifies that the test passes.