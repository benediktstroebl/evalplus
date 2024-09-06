```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    return [notes[ch] for ch in music_string.
# Test cases

music1 = 'o o| .| o| o| .| .| .| .| o o'
music2 = '1234'
music3 = 'www'
music4 = ' o o o| |' .' '| |.'
music5 = ''' o o o o o o o | o o o o o o | o o o o o o o o o o o o o'''
music6 = ''' o|.*'''

assert parse_music(music1) == [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
assert parse_music(music2) == []
assert parse_music(music3) == []
assert parse_music(music4) == []
assert parse_music(music5) == []
assert parse_music(music6) == []
```
This function `parse_music` parses a music string and returns a list of corresponding beat numbers.  The function is self-contained and its only purpose is to provide a way to parse and test music notation.