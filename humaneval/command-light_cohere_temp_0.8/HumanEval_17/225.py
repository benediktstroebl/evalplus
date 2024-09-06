```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    beats = music_string.split(' '|')
    notes_per_beat = [notes[beat[0]] for beat in beats]
    return [len(beats) * notes_per_beat[i] for i,beat in enumerate(beats)]

# Test cases
test_cases = [
    'o o| .| o| .| .| .| .| o o',
    'o o| .| .o| .',
    'o .| .|.',
    '|.| .|.'
]

# Function tests
for tc, music_str in test_cases:
    actual = parse_music(music_str)
    expected = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    assert actual == expected, f"Incorrect for test case: {tc}"
```
The above Python script provides a self-contained function `parse_music` that takes a music string in markdown format as input and returns a list of integers that represent the number of beats for each note in the music. The function uses a legend to define how long each note lasts, and then splits the string by '|' to separate the beats, it then uses the `notes` dictionary to map each beat to its corresponding number of notes. The `parse_music` function then provides a series of test cases to ensure that it is correctly parsing the music string.