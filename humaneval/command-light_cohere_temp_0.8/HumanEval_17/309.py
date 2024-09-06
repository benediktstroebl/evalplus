```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".";": 1,
    }
    return [notes[char] for char in music_string if char in notes]

# Test cases
test_cases = [
    "o o| .| o| .| .| .| .| o o",
    ",.",
    "oo",
    "oooo",
]

for test_case in test_cases:
    actual_result = parse_music(test_case)
    expected_result = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    assert actual_result == expected_result, f"Test case {test_case} failed"

print("All tests passed!")
```