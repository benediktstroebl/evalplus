```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o|.' : 2}
    return [notes[c] for c in music_string.test_music = ['o o|.', '|o', 'o', '|o', '.', 'o|', '.', '.', '.o']
    assert parse_music(''.join() == [1, 2, 1, 1, 2, 1])
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o o| .oo| o| o.oo') == [ dry_beat()
    assert parse_music('.'o.o| .o| .| .| .') == [1, 1, 1, 1]
```
This function 'parse_music' takes a music string in a format, where each character is either a note or empty, and then returns a list of integers representing the number of beats for each note. It uses a dry_beat to test its functionality.