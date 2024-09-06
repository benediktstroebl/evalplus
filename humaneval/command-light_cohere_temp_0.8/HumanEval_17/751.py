Here is a self-contained Python script that includes the function `parse_music` which solves the problem of parsing markdown music codes to a list of integers representing beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.format_notes_music('o o o| .| o| .| .| .| .| .| o o')

# Test cases
test_cases = [
    "o o| .| o| .| .| .| .",
    "o o| .| o| .| .| .| o",
    ".",
]

for test_case in test_cases:
    actual_result = parse_music(test_case)
    assert actual_result == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4], "Test case failed: {}".format_result()
```
This script defines a function `parse_music` that turns a markdown music code string into a list of integers representing the beats.  The test cases are provided, and are run to test the function.