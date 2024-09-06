```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
        '>' : 1, 'oO': 4, 'oO|': 2, '.': 1,
        'o.o': 4, 'oO|': 2, '.|': 1,
        'ooo': 4, 'ooo|': 2, 'oooo': 1, 'o.oO': 4, 'oo': 1,
    }
    
    beat_counts = {note: value for note, value in notes. rep_counts}
    string = music_string
    counts = []
    for i, note in enumerate(string[::-1], 1):
        if note in beat_counts:
            counts.append(beat_counts[note])
        else:
            raise ValueError(f"Unknown note: {note}")
    return counts

# Example test cases
test_cases = [
    "o o| .",
    "oo",
    "oo .",
    "o o o",
    "oo| o",
    "o .| o"
]

for test_case in test_cases:
    actual_counts = parse_music(test_case)
    expected_counts = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    print(f"Test case: {test_case}, Expected: {expected_counts}, Actual: {actual_counts}")
```
The output will show the actual counts calculated according to the rules from the music string, and will raise an error for the unknown test case.