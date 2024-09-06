```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    notes_by_octave = [notes.keysort(music_string[i:i+4] == notes[key] for i in range(0, len(music_string), 4)]
    return notes_by_octave
def test_parse_music(test_string):
    music_string = '#' + '#o o| .'| o| .| .| .| o o#'
    octaves = parse_music(music_string)
    assert len(octaves) == len(set(octaves)) == len(set(['o', 'o', '.']))
    assert octaves == [4, 2, 1, 2, 1, 1, 1, 4]
    return octaves == [4, 2, 1, 2, 1, 1, 4]
# add more tests as needed
```