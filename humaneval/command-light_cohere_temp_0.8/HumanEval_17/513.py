```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    music_notes = music_string.split(' ')
   
notes. strings on_of_note = []
    for note in music_notes:
        note_list = note.split('|')
        notes.append(int(note_list[0]))
    return notes

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(music_str)
    assert actual == expected
    music_str = 'Invalid Music'
    with pytest.raises(Exception):
        parse_music(music_str)
```
This script defines a function `parse_music` that takes a string of music notes and splits them by spaces, then returns a list of integers corresponding to the number of beats for each note. The `test_parse_music` function provides test cases, with the function's behavior verified and any exceptions caught, if any.