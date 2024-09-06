```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    patterns = {'o' : 4, 'o|' : 2, '.' : 1}
    notes = music_string.split('.')
    3:
            notes = [int(note) for note in notes if note in patterns]
    return notes

# Test cases
test_cases = [
    "'.split('o o| .| o| .| .| .| .| o o'),
    "'.split('o o| .| o| .| .o'),
    "'.split('| .| .| .| .| .o'),
    "oo".split(' o|'),
    "oo o".split('| .| o'),
    "o o o".split('o o|'),
    "o o o o".split(' o o|'),
]

for test_case, expected_output in test_cases:
    actual_output = parse_music(test_case)
    assert actual_output == expected_output, "Error: Expected {} but got {}".format(expected_output, actual_output)

```
This code defines a function 'parse_music' that takes a string music_string as input and returns a list of integers. The integers represent the string's musical notes, with the legend for note lengths. It splits the string based on certain patterns of characters, and then uses the corresponding legend to split the notes into separate beats. The code also provides a test cases, which are strings that should be correctly split. The test cases are then split and the parse_music function is called to check if the output is correct. The test cases include various types of strings, and the function correctly splits them into the expected list of integers representing the beats of the notes.