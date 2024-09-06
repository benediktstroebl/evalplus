Here's the provided Python code:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    return [notes[c] for c in music_string.parse(music_string)]

def test_parse_music():
    test_strings = ['o o| .| o| .| .| .| .| o o', '.' # missing whole note
                 'o o| .', 'o|.' # missing half note
                 '.|' # missing quarter note
                 'o| .| .| ' # extra character
                 'oo|.' # extra o
                 ]
    for test_string in test_strings:
        got = parse_music(test_string)
        expected = [4, 2, 1, 2, 1, 1, 1, 4, 4]
        assert got == expected
```

The code defines a function **`parse_music`** that takes a string of music notes and returns a list of integer beat durations. The function uses a legend to map music note characters to their beat duration values. The test_parse_music function contains a collection of test strings and runs them through the **`parse_music`** function to ensure the function is working as expected.