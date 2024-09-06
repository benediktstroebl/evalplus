```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    beats = [notes[c] for c in music_string.split(' '|')]
    return beats
def test_parse_music():
    music = 'o o| .| o| .| .| .| .| o o'
    beats = parse_music(music)
    assert len(beats) == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4] and all(beat == 4 for beat in beats)
    assert len({beat for beat in beats}) == {4, 2, 1, 2, 1, 4}
    assert all(beat == 4 for beat in beats)
    music = '.' * 5
    beats = parse_music(music)
    assert len(beats) == 5
    assert beat == 4 for beat in beats
```