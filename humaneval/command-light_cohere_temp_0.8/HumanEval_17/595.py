```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")")
   
    parse_notes = [int(x) for x in notes if x.isdigit()]
    whole_notes = 0
    half_notes = 0
    quarter_notes = 0

    for note in parse_notes:
        if note == "o": whole_notes += 4
        elif note == "o|": half_notes += 2
        elif note == ".":": quarter_notes += 1
        else:
            raise ValueError("Invalid note: " + note)

    return [whole_notes, half_notes, quarter_notes]

# Example tests
def test_parse_music():
    music_str = "o o| .| o| .| .| .| .| o o"
    notes = parse_music(music_str)

    assert notes == [4, 2, 1, 2, 2, 1, 1, 1, 4]

# Run the test suite
test_parse_music()
```
This script defines a function `parse_music` that takes a string of music notes as input and returns a list of integers corresponding to the number of beats in each note. The `test_parse_music` function contains tests to check if the `parse_music` function works correctly. The test suite runs the