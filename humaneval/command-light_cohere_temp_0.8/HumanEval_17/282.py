```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes.get(note) for note in music_string.beats = [len(beats)
    return beats

# Test
def test_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected_beats = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    actual_beats = parse_music(music_str)
    assert actual_beats == expected_beats, f"Expected {expected_beats}, got {actual_beats}"

test_music()
```
This code defines a `parse_music` function that parses a music string in a specific format and returns a list of integers representing the number of beats for each note. The test function, `test_music`, creates a music string, calls the `parse_music` function, and asserts that the resulting beats are equal to the expected beats. This code follows the guidelines and provides a clear and readable solution.