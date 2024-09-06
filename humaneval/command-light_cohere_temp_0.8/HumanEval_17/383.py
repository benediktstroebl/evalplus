```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
        '.' : 1, 'oO': 4, 'O|': 2, 'OA': 1,
    }
    return [notes[note] for note in music_string.test_parse_music("o o| .| o| .| .| .| .| o o")]
```
This function, `parse_music`, accepts a string music_string in a format that represents a sequence of musical notes, and returns a list of corresponding beat counts. The function leverages a legend: whole note (o), lasts four beats; half note (o|), lasts two beats; and quarter note (.), lasts one beat. The input string is parsed and the notes are extracted using a dictionary mapping.

This function is a standalone and self-contained solution that can be used to solve the problem of parsing a musical notes representation into a list of beat counts.