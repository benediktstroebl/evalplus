```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.type(str):
    return [int(x) for x in notes.
    return [x

    assert all(x == 4 for x in music_string.note[0:4]), "First note is not a whole note.")
    assert all(x == 2 for x in music_string.replace(2:)), "Half notes are missing.")
    assert all(x == 1 for x in music_string.order(1:)), "Quarter notes are missing.")
    assert all(x == 4 for x in music_string.group()), "Notes are not separated by dashes.")
    return [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
```