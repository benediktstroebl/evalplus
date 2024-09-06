```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    
    beats = [notes[c] for c in music_string.strip(). Note that the saw an opportunity to match each possible note with a key in notes.
    return beats

    # Example tests
    assert parse_music('o o| .| o| .| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('| .| .| .') == [1, 1]
    assert parse_music('o ot') == [2]
    assert parse_music(' | .') == []
    assert parse_music(''). == []
```
This script defines a function **`parse_music`** that takes a string of music notes as an input and returns a list of integers representing the number of beats corresponding to each note.