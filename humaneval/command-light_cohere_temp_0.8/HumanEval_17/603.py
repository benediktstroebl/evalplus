```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    notes_lengths = [4, 2, 1]

    beats = []
    for note in notes:
        beats.append(notes_lengths[note] * len(music_string[::note]))

    return beats

# Test cases
music_cases = [
    "o o| .| o| .| .| .| .| o o",
    "o o| .| o| .| .| .| .",
    "|o||.",
    "o o o o o",
    "o o o",
]

for music_case, expected_beats in music_cases:
    actual_beats = parse_music(music_case)
    assert actual_beats == expected_beats, f"Case {music_case} expected {expected_beats}, got {actual_beats}"
``` 
This script defines a function `parse_music` that parses a music string and returns a list of its beat lengths. The function is then implemented with several test cases to ensure its correctness.