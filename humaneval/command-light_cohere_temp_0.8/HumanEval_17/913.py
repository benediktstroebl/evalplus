```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beats = music_string.split(' ')
    whole note')
    for note in whole_note:
        if note in notes:
            beats.append(notes)
    else:
            beats.append(beats[-1] * 2)
    return beats

# Test cases
test_parse_music = [
    'o o| .| o| o| .| .| .| .| o o',
    'o o o o o o o o',
    ']| |o| ',
    'o o o o| o ',
    ' o o| .o',
    ' o o o o| .| ',
    ' .o .o',
    ' .| o| .',
    ' o o o o o o',
    ' .o o o o',
    ' .o o o o o',
    ' o .o o',
    ' o o o o o| ',
    ' o o o o o| o o o o',
    'o o o o o o o',
]

for case in test_parse_music:
    actual_beats = parse_music(case)
    print(f"Case: {len(actual_beats)}, {len(expected_beats)})
```
The function parse_music takes a string of music notes in a specific format. It returns a whole a list of beats, where each beat corresponds to a whole note. The test cases will print the correct beats for each test case.