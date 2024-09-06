```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    beat = 1
    notes_count = [0] * 4
    for symbol in music_string:
        if symbol in notes: notes_count[notes.index(symbol)] += beat
        beat += 4
        return notes_count
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected_result = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual_result = parse_music(music_str)
    assert actual_result == expected_result, "Function doesn't return the expected result."
test_parse_music()
```