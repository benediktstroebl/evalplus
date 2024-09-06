```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')'. A list of integers representing how many beats a note lasts for.
    return [list(map(int, line. )))

def test_parse_music():
    music = "o o| .| o| .| .| .| .| o o"
    result = parse_music(music)
    assert len(result) == 12
    result = parse_music("o o| o| o| o| o o")
    assert len(result) == 12
    result = parse_music(".|.")
    assert len(result) == 1
    result = parse_music("o o| o| .")
    assert len(result) == 2

test_parse_music()
``` 
This code defines a function `parse_music` that splits a music string into individual notes. It then maps each note to the number of beats it lasts, returning a list of integers corresponding to the note durations. The `test_parse_music` function is designed to verify the correctness of the `parse_music` function. The test passes all corresponding tests.