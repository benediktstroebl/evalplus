```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    return [int(beat) for beat in music_string.partition_beats_list() if beat.

def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| .| o o'
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```