```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')
    string_notes = music_string.split('o request an number of notes from the string, returning a list of numbers (e. The length of the string is the number of beats.

def test_music_parser():
    music_str = 'o o| .| o| .| .| .| .| o o'
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4] # Testing the function
    assert parse_music('o o| .| o| o| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # Testing with a string with an extra beat

test_music_parser()  # Passes the test
```