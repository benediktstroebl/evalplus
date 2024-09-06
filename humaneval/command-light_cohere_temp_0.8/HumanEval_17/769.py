```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    beats = [notes.get(x, notes. a=beats[music_string[i:]) for i in range(len(music_string))]
    return beats

# Test cases
music_cases = [
    "o o| .| o| .| .| .| o o",
    ",.|.| .| .| .| .| .",
    "oo",
    "o o-",
    "|o\.",
    "oo| ",
    " .ooo",
    " o o o",
    "oooo",
    "-ooo",
]

for music_test in music_cases:
    actual_beats = parse_music(music_test)
    expected_beats = [4, 2, 1]  # Corresponding to legend
    print(f"Test: {music_test}, {actual_beats}, {expected_beats}")
``` 
This script defines a function `parse_music` that parses and returns a list of beats from a given music string. It then provides a several test cases, and the function's output is compared to the expected beats. This self- the example shows how the results of running the function against different music strings.