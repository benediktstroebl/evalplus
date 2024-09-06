```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')').
    notes = {k: int(b) for k, b in enumerate(beats)}
    return [notes[char] for char in music_string if char in notes]

def test_parse_music():
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This code defines a function `parse_music` that takes a music string in the "O" format and returns a list of beats. The function splits the music string into separate notes and then uses a dictionary to map these notes to the number of beats they last. The `test_parse_music` function verifies that `parse_music` correctly parses the music string.