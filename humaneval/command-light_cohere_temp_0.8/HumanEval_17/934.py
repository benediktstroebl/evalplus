```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
    }
    return [notes.get(beat) for beat in music_string.get(r":', '').

# Basic tests
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

# Complex tests
def test_complex_cases():
    music_str = 'o o| .|.| o| .| .| .| .| o o'
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    music_str = '.|o o|...'
    assert parse_music(music_str) == [1, 4, 4]

    music_str = 'o o/o o'
    assert parse_music(music_str) == [4, 4, 4]

    music_str = '..|...'
    assert parse_music(music_str) == []

test_parse_music()
test_complex_cases()
```
This script defines a function **`parse_music`** that parses a music string in a recognized format and returns a list of integers representing the duration of each beat. The script also contains a basic and complex test cases to validate the correctness of the **`parse_music`** function.