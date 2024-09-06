Below is a Python script that defines a self-contained function that solves the problem of parsing musical notes in a string and returns a list of integers representing the duration of each note.

```python
import typing
def parse_music(music_string: str) -> typing.List[int]:
    string must be in the format 'o o| .| .' .'.

    notes = {
        'o': 4,
        'o|' : 2,
        '.' :  1,
        'oO' : 4,
        'O' : 2,
        'oo' : 2,
        'oo|' : 1,
        'oooo' : 4,
        'Oooo' : 2
    }

    notes_in_string = music_string.get(infix)

    if notes_in_string:
        return [notes[note] for note in notes_in_string]
    else:
        return []
```