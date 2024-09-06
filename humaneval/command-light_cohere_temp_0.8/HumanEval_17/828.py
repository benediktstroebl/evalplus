```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = {'o' : 4, 'o|' : 2, '.|' : 1}
    return [beats[note] for note in music_string.

def test_parse_music():
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o o| o| .| o| .| .') == [4, 4]
    assert parse_music('.|') == []
    assert parse_music('a') == []
    assert parse_music('z') == []
```
The function parse_music takes a string music_string in a format of a series of notes, each separated by a space, and returns a list of integers corresponding to the number of beats for each note.  The script then defines a dictionary beats with musical note characters as keys and the number of beats the note will last as values. The parse_music function uses this dictionary to parse the music_string and returns a list of integers representing the number of beats for each note. The test_parse_music function then verifies that the parse_music function behaves as expected by running it with a variety of test cases and asserting the resulting lists of integers match the expected values.