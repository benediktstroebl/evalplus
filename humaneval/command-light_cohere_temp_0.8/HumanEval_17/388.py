```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    pattern = r'\b(o|o\^|.){|.\b'
    matches = pattern.findall(music_string)
    return [notes[note] for note in matches]
def test_music() -> None:
    music_str = 'o o| .| o| .| .| .| o o'
    expected_beats = [4, 2, 1, 2, 1, 1, 1, 1, 4]
    beats = parse_music(music_str)
    assert beats == expected_beats
    return
test_music()
```