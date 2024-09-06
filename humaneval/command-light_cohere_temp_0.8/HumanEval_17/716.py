```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') |
   
    notes = [int(note.strip()) for note in notes]
    return notes

def test_parse_music(test_string):
    music_notes = parse_music(test_string)
    assert len(music_notes) == 17, "Error: Music string has %d notes, expected 17" % (len(music_notes)-1)
    assert all(type(note) == int for note in music_notes), "Error: Music string notes are not integers"
    return music_notes
```