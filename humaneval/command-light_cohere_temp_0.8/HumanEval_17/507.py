```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') | [.] Roman numeral system.
    notes = [ ]
    notes.
    notes = [reversed(notes)
    notes = [int(note.strip() for note in notes])
    return notes

# Test cases
def test_parse_music():
    music_str = 'oo o| o|.| o| o| .| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    notes = parse_music(music_str)
    assert notes == expected
```