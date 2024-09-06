Here's the improved version of the Python script with self-contained function and tests:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.
    This task is legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Returns: list of integers corresponding to how many beats each note lasts.
    """
 test_parse_music_test = [
        "o o| .| o| o| .| .| .| .| o o",
        "oo",
        "o o O| o o O",
        "  o o  ",
        " o o  |  o ",
        "oo o",
        "o o O",
        " o o O o",
        " o o o o o",
        " o o O O",
        "oo o o",
        ".",
        " o ",
        ]
    notes = parse_music(test_parse_music_test)
    assert len(notes) == len(test_parse_music_test)
    assert all(type(note) == int for note in notes)
    assert all([4, 2, 1 for beat in range(len(notes)) for note in test_parse_music_test[beat: beat+1]])
    return notes
``` 
This version of the code provides a self-contained function with tests using the `test_parse_music_test` list that covers various inputs and edge cases.  The also maintains the status of the code and function.