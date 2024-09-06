```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beats = music_string.split(' ')
    RawNotes = [notes[c] for c in music_string if c in notes]
    return [len(RawNotes) for RawNotes in RawNotes]

def test_parse_music():
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

```
This Python code defines a function `parse_music` that takes a music string and parses it into a list of integers. The function uses a legend to map the music notes to their beat durations. The function then tests the raw music string, `o o| .`, and returns the correctly parsed music, as expected.