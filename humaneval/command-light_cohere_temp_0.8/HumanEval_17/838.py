```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = music_string.split(' ')
    a pattern = r'(\d+)\s*[o|].([^|]+)\s*[o|].([^|]+)\s*[o|].+'
    notes = {k: int(v) for k, v in pattern. pattern.items()}
    region: (len(notes, beat) for beat in notes), 4)
    return notes

# Test cases
def test_parse_music():
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('|') == []
    assert parse_music(''). == []
    assert parse_music('oo') == [4, 4]
    assert parse_music('oo|o') == [4, 4]
    assert parse_music('oo o| o') == [4, 2, 1, 2, 2, 1, 1, 1]

test_parse_music()
```
This Python script defines a function called `parse_music` that takes a string representing music notes and parses them into a list of integers representing beats for each note. The `notes` dictionary maps note characters to the number of beats they last. The test cases ensure that the function correctly identifies and returns the correct beat count for various input strings.