```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.parse(music_string)]

def test_music():
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

# Run the test function
test_music()
```
This script defines a function `parse_music` that parses a music string and returns a list of integers representing the duration of each note in the string. The function uses a `notes` dictionary that maps musical symbols to their respective durations (whole, half, quarter). The `parse_music` function uses the `notes` dictionary to split the music string into individual notes and then returns their durations. The test function `test_music` asserts that the `parse_music` function correctly identifies and classifies the notes in the input string. This way, it tests the provided string and ensures the function's correctness.