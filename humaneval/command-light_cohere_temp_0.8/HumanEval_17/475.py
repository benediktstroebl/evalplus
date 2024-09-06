```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1
    }
    beat_counts = {note: notes[note] for note in notes}
    return [beat_counts[note] for note in music_string.

# Test cases
test_strings = [
    "o o| .| o| o",
    ".",
    "o o o o o",
    "| o| .| o| .",
    "oo o o| o|",
]

test_results = []

for test_string in test_strings:
    results = parse_music(test_string)
    test_results.append(results)

for result, expected in zip(test_results, [4, 2, 1, 2, 1, 2, 1])):
    print(f"Test: {test_string} => Expected: {expected}, Actual: {result}")
```