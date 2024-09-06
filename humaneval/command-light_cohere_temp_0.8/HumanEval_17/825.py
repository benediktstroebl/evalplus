```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')')
    notes
    for note in notes:
        note = note.split('o rule:
            if note[0] == 'o':
                note = [4]
            elif note[0] == 'o|':
                note = [2]
            elif note[0] == '.|':
                note = [1]
            else:
                raise ValueError(f"Invalid note: {note}.")
        yield note

# Test cases
test_cases = [
    'o o| .| o| o| .| .| .| .',
    'o o| .| o| o| .| .| .',
    'o| o| o| o| |.',
    '|.o| .o| .',
    'o o o| .',
]

# Function call and result validation
for test_case in test_cases:
    actual_notes = parse_music(test_case)
    expected_notes = [4, 2, 1, 2, 1, 4, 4, 4]  # From the parse_music function
    assert actual_notes == expected_notes, f"Incorrect notes found in '{test_case}'.
```
This Python code defines a function called `parse_music` that parses a given music string and produces a list of integers. The function splits the input into individual notes, which are then processed according to their musical notation rules. The code also includes a list of test cases, and for each test case, the function is called to produce the expected notes. The code then validates whether the actual notes generated match the expected notes, using the `assert` statement.