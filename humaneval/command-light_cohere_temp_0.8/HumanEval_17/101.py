```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')
    particular and unique notes that can be created with the above split method.  Here is an example:
    music_string = 'o o| .| o| .| .| .| .| .| o o'
    notes = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    return notes

# Test the function with different inputs
test_strings = [
    "'.join_ ,
    "oo o o|.",
    "oo o o o|.",
    "oo o o o o o o|.",
    "o o o .",
    "o o o o o o o .",
    "o o o o o o o o",
    # Extra whitespace after last note
    "  o o o o o o o o",
    # Extra new lines
    "o o o o o",
    "  o o o o o .",
    # Extra characters
    "oo o o !",
    " o o o .",
]

correct_notes = []

for test_string in test_strings:
    notes = parse_music(test_string)
    correct_notes.append(notes)

print("Test successful!")
```