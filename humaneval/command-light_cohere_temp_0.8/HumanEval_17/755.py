```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
        '.': 1
    }
    
    beat_counts = [notes.get(char, 4) for char in music_string if char in notes]
    
    return beat_counts

# Test cases
test_cases = [
    'o o| .| o| .| .| .| .| o o', [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
    '.|o| .| .| .| .| .| o', [1, 1]
    'o\n o o', [4]
    '|o\n|o|', [1]
]

for test_case, expected_beats in test_cases:
    actual_beats = parse_music(test_case)
    assert actual_beats == expected_beats, f"Expected: {expected_beats}, Got: {actual_beats}"
 ``` 
This script defines a function `parse_music` that takes a music string as input and returns a list of integers corresponding to the number of beats that each note lasts. The function uses a legend to map notes to their respective beat counts, and the input music string is split into characters to extract the notes.