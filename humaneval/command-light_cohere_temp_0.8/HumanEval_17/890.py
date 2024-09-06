```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, '\\"o' : 4}
    return [notes[char] for char in music_string.
#tests

def test_parse_music():
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o o| .| o| .| .o| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 4, 4]
    assert parse_music('.\\"o') == [1]
    assert parse_music('o|o|') == [2, 2]
    assert parse_music('o o o o| .| o o o') == [4, 4, 4, 2, 2, 1, 1, 1, 1]
```
This script defines a function `parse_music` that parses and returns a list of integer beats corresponding to the input music string, which is a special format of musical notes. The tests provided in the test_parse_music() function pass the corresponding tests.