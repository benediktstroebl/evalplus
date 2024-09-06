```python
from typing import List

 Patterns = {
    'o': 4,
    'o|': 2,
    '.|': 1,
}


def parse_music(music_string: str) -> List[int]:
    result = []
    notes = []

    current_note = None
    i = 0

    while i < len(music_string):
        if music_string[i] in 'o|.|':
            if current_note is not None:
                notes.append(current_note)
            current_note = Patterns[music_string[i]]
            i += 1
        elif current_note is not None:
            current_note -= 1
            if current_note == 0:
                notes.append(current_note)
                current_note = None
        i += 1

    if current_note is not None:
        notes.append(current_note)

    return notes
``` 

This script leverages a `dict` called `Patterns` to map note patterns to their beat lengths. The `parse_music` function reads a string of musical notation and computes the corresponding list of beats. 

The script assumes the input follows the given ASCII format and that one can have multiple notes in a single call. You can verify the functionality of the script by invoking the test cases provided in the original task.