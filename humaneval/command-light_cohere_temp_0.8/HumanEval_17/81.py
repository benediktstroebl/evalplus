```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[char.find(c) for c in music_string] for char in music_string]

def test_parse_music():
    music_str = "o o| .| o| .| .| .| o o"
    parsed = parse_music(music_str)
    assert parsed == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
The code defines a function `parse_music` that takes a string representing a musical score and parses it into a list of integers representing the duration of each note in the piece. It uses a specific dictionary (`notes`) to map the notes to their respective durations (whole, half, quarter). The test function, `test_parse_music`, creates a music score and runs the `parse_music` function to check if the parsed score is correct.