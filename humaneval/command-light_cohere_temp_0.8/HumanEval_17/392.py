```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') |
    whole, half, quarter ->  [int(whole) * 4, int(half) * 2, int(quarter)]
    return [int(x) for x in notes]

# Test cases
test_cases = [
    "o o| .| o| .| .| .| .| o o", [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
    "o o| o| .", [4, 2, 1]  # Should return [4, 2, 1, 2]
    "|o o| .", [1, 4]  # Should return [1, 4]
    " ".|.", [1]  # Should return [4]
]

for test_case, expected in test_cases:
    actual = parse_music(test_case)
    assert actual == expected, f"Case {test_case} failed"
```  This Python code defines a function `parse_music` that parses a music notation string and returns a list of note durations. The function splits the expected notes based on rules (whole, half, quarter), then multiplies the corresponding durations by their respective note values. The test cases validate the expected results are printed for various inputs.