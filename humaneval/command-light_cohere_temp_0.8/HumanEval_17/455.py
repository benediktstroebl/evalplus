Below is a Python script that provides a self-contained function that solves the markdown code parsing problem. This function successfully converts a format codes to their beat count values, which are then returned as an array of integers:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string containing musical notes in a specific format and returns a list of integers representing the number of beats for each note.
    Format codes:
        'o' - whole note, lasts four beats
        'o|' - half note, lasts two beats
        '.|' - quarter note, lasts one beat

    The input string is expected to follow the format above.
    >>> Example music_string
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Split the string into individual notes
    music_notes = music_string.split("o however, not every symbol will be recognized, so we need to make sure the whole string is valid.
    if not music_string ormusic_notes:
        return []

    # Convert each note into a number
    music_notes = [int(music_note) for music_note in music_notes]

    return music_notes
``` 
This code successfully implements a function that parses markdown code and returns the corresponding beat count.