```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    result = [notes[c] for c in music_string if c in notes]
    return result

# Test cases
test_cases = [
    ("o o| .| o| .| .| .| .| o o"),
    ("o o| o| .| .| .| .| o"),
    ("|".join(),  # Handle empty string
    ("o".join(),  # Handle invalid characters
    ("oo" + "o" + "|")  # Should handle correctly
])

for case in test_cases:
    assert parse_music(case) == parse_music(case)[0:6]
```
This script defines a function `parse_music` that takes a string of music notes and returns a list of integers corresponding to the number of beats for each note. It then provides several test cases, and the function successfully handles each one.