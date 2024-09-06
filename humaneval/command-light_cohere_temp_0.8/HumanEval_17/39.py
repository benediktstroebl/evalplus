```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o', '|', '|', 'o', 'o', '.', 'o', 'o', '.']
    form = ' '.join(notes)
    music_string = music_string.split(form)

    times = [int(beat) for beat in music_string[0::len]]
    pitch = [int(note) for note in music_string[1::len]]

    return pitch
def test_parse_music():
    music_str = "o o| .| o| .| .| .| o o"
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    music_str = "o o| /| .| o| .| .| .| o o"
    assert parse_music(music_str) == [4, 2, 1, 2, 1, 4, 1, 1, 1, 2, 2]
```
This script defines a function `parse_music` that takes a string of music notes in a special ASCII format, then returns a list of corresponding integers, indicating how many beats each note lasts. The script also has a function `test_parse_music` that contains test cases with different music strings, and asserts the correct results of the `parse_music` function for each test.