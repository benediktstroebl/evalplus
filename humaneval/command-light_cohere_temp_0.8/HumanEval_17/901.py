```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    result = [notes[note] for note in music_string.
    return result

    # Test cases
    test_cases = [
        'o o| .| o| .| .| .| .| o o',
        'oso',
        'ho o',
        '|oo',
        'oooo',
        'o o o o o| o|',
    ]

    expected = [4, 2, 1, 1, 1, 4, 4, 4, 4]
    for test, expected_result in zip(test_cases, expected):
        actual_result = parse_music(test)
        assert actual_result == expected_result, "Expected: {}, got: {}".format(expected_result, actual_result)
```
This code defines a function `parse_music` that parses a music_string, represented as a string of notes in the "music script" The notes are defined in the notes dictionary, with keys as the note characters and values as the number of beats that the note lasts. The `parse_music` function loops through the music_string and returns a list of integers, corresponding to the number of beats of each note.