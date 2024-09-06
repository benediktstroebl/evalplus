```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', 'o', '.', 'o', 'o']
    pattern = [i for i in notes if i in music_string]
    return pattern

# Test cases
test_cases = [
    "o o| .| o| .| .| .| o o",
    "   o  ",
    "oo o  ",
    "  o|   ",
    "oo  o| ",
    "  .|  ",
    "  o  o",
    # Incorrect: missing ending slash
    "  o o",
    # Incorrect: other characters instead of notes
    "oo aa",
]

for case in test_cases:
    actual_notes = parse_music(case)
    expected_notes = [4, 2, 1, 2, 1, 1, 1, 4, 4]  # From the parse_music function
    print(f"Case: {case} => {actual_notes, expected_notes})
```