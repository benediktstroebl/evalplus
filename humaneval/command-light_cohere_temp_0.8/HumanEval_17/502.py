Here's a self-contained Python script that solves the problem you provided:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        others: []
    }
    beats = []
    for note in music_string.split(' '.' Music 'o| '|.'):
        if note in notes:
            beats.append(notes)
        notes[note])
    return beats

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected_beats = [4, 2, 1, 2, 1, 1, 1, 1, 4]
    beats = parse_music(music_str)
    assert beats == expected_beats
    music_str = '.' * 43
    expected_beats = []
    beats = parse_music(music_str)
    assert beats == expected_beats

# Main function call
test_parse_music()
```
This script defines a `parse_music` function that takes a music string in the format you provided and returns a list of beats corresponding to the notes. It also provides test test cases to verify the function's behavior.