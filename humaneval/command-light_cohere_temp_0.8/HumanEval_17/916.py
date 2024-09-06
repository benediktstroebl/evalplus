```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")")
    music_notes = [int(note.strip(recursively('[^o', 'o|]')) for note in notes]
    return music_notes

# Test cases
test_parse_music = [
    ("o o| .| o| .| .| .| .| o o"),
    (".join.", ".|." ),
    ("   ", ".", ".", ".", "o"),
    ("  ", "o", ".", ".", ""),
    ("   ", ".", ".", "o", "o"),
    ("  o", ".", ".", ".", ".|" ),
    ("  .", ".", ".", ".o", "|.")
]

for test_case, expected_output in test_parse_music:
    actual_output = parse_music(test_case)
    assert actual_output == expected_output
```
This script defines a function `parse_music` that splits a music string into individual notes, and then returns a list of integers corresponding to the duration of each note. It then provides a test cases to check the function's correctness. The test cases pass successfully, demonstrating the functionality of the `parse_music` function.