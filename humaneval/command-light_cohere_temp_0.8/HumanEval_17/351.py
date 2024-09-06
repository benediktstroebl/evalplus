```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    return [notes[note] for note in music_string.test_music = ['o o o| .| .| .| o o', 'oo', '.', 'oooo', 'o|', '.o']
    assert parse_music(test_music) == [4, 2, 1, 2, 1, 4]
 ```

This function takes a string of music notes in a specific format and returns a list of integers that represents how many beats each note lasts.  The function uses a predefined dictionary to map the musical notes to the number of beats.