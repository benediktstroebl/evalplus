Here's a Python script that demonstrates the solution to the markdown code block music note parsing problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.test_music('o test_music("o o| .| o| .| .| .| .| .| o o")
 assert parse_music("o o| .| o| .| .| .| .| o o") == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a `parse_music` function that takes a music string and returns a list of integers representing the number of beats for each note. The function uses a legend provided in the docstring to define the mapping of notes to beat count. The test_music function is then used to validate the `parse_music` function with the provided music string.