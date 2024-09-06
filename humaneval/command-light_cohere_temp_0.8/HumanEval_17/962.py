```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        others: []
    }

    beats = 0
    current_beat = 0

    for symbol in music_string:
        if symbol in notes: beats += notes[symbol]
        current_beat += 1

        if current_beat == 4:
            current_beat = 0

    return beats

#Test
test_cases = [
    "o o| .| o| .| .| .| .| o o'",
    "4 4|8|2|3 8|2 3|2|1|8|1 6|2",
    "o o| o| .",
    "4 4|8|2|3 8|2 3|2|1",
    "o o o o o o o",
]

for test_case in test_cases:
    actual_beats = parse_music(test_case)
    expected_beats = [4, 4, 2, 2, 1]

    print(f"Test Case: {test_case}\n{actual_beats}\n{expected_beats}\n")
    assert actual_beats == expected_beats
``` 
This code defines a function `parse_music` that takes a string music_string as input and returns the number of beats that each symbol represents in the string will play (whole note, half note, quarter note). The `beats` variable keeps track of the number of beats played so far, and `current_beat` counts the number of beats until the current symbol is over 4 beats.  The `parse_music` loops through each symbol in the string and counts the number of beats it represents. The code also implements a test cases that cover a variety of music strings and asserts that the `parse_music` function returns the correct number of beats for each input.