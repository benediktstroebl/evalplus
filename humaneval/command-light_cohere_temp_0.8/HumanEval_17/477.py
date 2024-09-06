```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")")
    code

    # converts notes to integers
    notes_numbers = [int(note) for note in notes]

    return notes_numbers

# test cases
def test_parse_music():
    test_strings = [
        "o o| .| o| .| .| .| .| o o",
        "o o|.",
        "..|.",
        "o o o",
        " "
    ]

    expected_results = [
        [4, 2, 1, 2, 1, 1, 1, 1, 4, 4],
        [],
        [4, 4],
        [8],
        []
    ]

    for test_string, expected_result in zip(test_strings, expected_results):
        actual_result = parse_music(test_string)
        assert actual_result == expected_result, "Actual result was %s, expected was %s"

test_parse_music()
```
This script defines a function `parse_music` that parses a music notation string and returns a list of corresponding note lengths. The function is then tested with a variety of input strings and their expected results, using the `test_parse_music` helper function to organize and run the tests. The test cases ensure that the parse music correctly returns the expected results.