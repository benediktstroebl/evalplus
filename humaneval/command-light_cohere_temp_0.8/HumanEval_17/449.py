Here is a self-contained Python function that solves the problem you provided:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')'). How many beats is each note?
notes = [int(note) for note in notes]
    return notes

# Test cases
test_cases = [
    "o o| .| o| o| .| .| .| o o",
    "o o| .| o| .| .| .| o",
    "oo",
    "o\no",
    "",
]

for test_case in test_cases:
    actual_notes = parse_music(test_case)
    expected_notes = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]  # Reference from the function definition
    assert actual_notes == expected_notes, f"Error in test case: {test_case}"

```
This Python function, **`parse_music`** accepts a music string as input and yields a list of integers that reflect the number of beats in each note. The function splits the by '|' the input music string to identify the beat of each note, and then converts each note to an integer using the **`int()`** function. 

This approach ensures that the code is concise and easy to maintain, as it contains only the essential logic for solving the problem. It also eliminates the this need for external libraries or modules, which would increase complexity and potentially introduce compatibility issues.