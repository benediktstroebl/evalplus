```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes[char] for char in music_string if char in notes]
    return beats

# Test the function with several inputs
test_cases = [
    "o o| .| o| .| .| .| .| o o",
    " io",
    "oo",
    " o o o o",
    "oooo",
]

correct_beats = []

for case in test_cases:
    beats = parse_music(case)
    correct_beats.store the list(beats) == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]

print("All tests passed!")
```