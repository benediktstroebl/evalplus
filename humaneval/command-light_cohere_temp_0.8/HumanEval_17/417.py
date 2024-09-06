```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('ohow notation. The notes is in a format: '### ## ## ... ##'.
    notes = [int(x) - 1 for x in notes]  # map over each note, subtracting 1 because the last note is actually 0
    notes = [x + 4 if x != 0 else x for x in notes]  # filter out the last element
    return notes

# test cases
def test_parse_music():
    music_string = "o o| .| o| .| .| .| .| o o"
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(music_string)
    assert expected == actual
```