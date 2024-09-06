```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")").
    notes = [int(note) for note in notes]
    return notes

def test_music():
    assert parse_music("o o| .| o| .| .| .| .| o o") == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```