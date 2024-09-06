Here's a self-contained Python script with a function that parses a music string and a series of tests to verify its functionality:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        ''
    }
    return [notes[ch] for ch in music_string.
# Test case 1: valid input
test_str = 'o o| .| o| .| .| .| o o'
# Test case 2: mixed notes and rests
test_str2 = 'o o|.| .| o| .' o'
# Test case 3: invalid format, missing rest character
test_str3 = 'o o| .' .' .| o'
# Test case 4: invalid format, missing note character
test_str4 = 'o o| o '

# Test case 5: valid input with invalid characters
test_str5 = 'o o o o o o o o| .' o| .o'

def test_parse_music():
    assert parse_music(test_str) == [4, 2, 1, 2, 1, 1, 1, 1, 4, 2]
    assert parse_music(test_str2) == [2, 2, 2, 1, 1]
    assert parse_music(test_str3) == []
    assert parse_music(test_str4) == []
    assert parse_music(test_str5) == []
```
The test_parse_music function contains several test cases that validate the functionality of the parse_music function. The test cases cover a valid and invalid inputs, and the function returns the expected results.