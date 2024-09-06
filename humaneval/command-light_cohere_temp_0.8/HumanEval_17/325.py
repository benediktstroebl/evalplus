```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.test_music_parse(music_string)]

# Test code
def test_music_parse(music_string):
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
    actual = parse_music(music_string)
    assert actual == expected, f"Expected [{expected}], but got [{actual}]"
```
This code defines a function `parse_music` that parses a music string into a list of beat counts, and a function `test_music_parse` that tests the `parse_music` function with various music strings. 
The `parse_music` function uses a dictionary to map music note characters to their respective beat count values, and returns the beat count list. The `test_music_parse` function provides a number of test cases to ensure the `parse_music` function is working correctly.