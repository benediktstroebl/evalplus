```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        ".":o": 4,
        ".":o|": 2,
        ".:": 1,
        ";.": 1,
        " "; 0,
    }
    beats = music_string.split(" ")
    beats = [beat.split(" "). "o") for beat in beats]

    return [notes[note] for note in music_string.split(" ").beat]

# Test cases
test_strings = [
    "o o| .| o| o| .| .| .| o o",
    "o o| .",
    ".",
    "oo",
    ".",
    "oo o",
    "oo o| ",
]

test_cases = [test_string for test_string in test_strings]

for test_case in test_cases:
    notes = parse_music(test_case)
    assert len(notes) == len([range(beat) for beat in test_case.split("o.beat")
    reasonable lines=[note * beats for note in test_case.split("o long note.")])
    assert len(notes) == sum(lines)
```

The above code defines a function `parse_music` that takes a string of music notes and returns a list of integers corresponding to the number of beats in each musical note. The function uses a legend of musical notes to create a mapping of note characters to the beat counts. The test cases are defined as well, to test the correctness of the function.