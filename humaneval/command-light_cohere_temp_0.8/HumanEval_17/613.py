```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes[note] for note in music_string.parse("").

def test_parse_music():
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('.' == [0])
    assert parse_music('o o o o o| .') == [4, 4, 4, 4, 4]
    assert parse_music('|.' == [1])
    assert parse_music('|oo|') == [1]
    assert parse_music('abc|def|ghi') == []
```
The function `parse_music` takes a string music_string as input and returns a list of integers. The function is using a dictionary `notes` which maps musical notes to the duration (in beats) that those notes last. The function uses the str.code the music string line by line and returns the result. The test_parse_music function tests the function `parse_music` by asserting that it returns the correct result for each test case.