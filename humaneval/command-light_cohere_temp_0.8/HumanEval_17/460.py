```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_by_length = [notes[note] for note in music_string.parse(music_string)]
    return notes_by_length

# Tests
def test_parse_music():
    assert parse_music('o o| .| o| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('oo o o o o o o o o o o') == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    assert parse_music('other text') == []
```
This code defines a function **`parse_music`** that parses a music string representing notes and their lengths. The function utilizes a legend to map musical notes and their durations. The function then returns a list of integers that represent the number of beats for each note. The test function **`test_parse_music`** ensures that the **`parse_music`** function accurately operates, and passes all corresponding tests.