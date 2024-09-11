```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the duration of each note.

    The input string should be in the following format:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    music_list = music_string.split()
    parsed_music = [note_durations[note] for note in music_list]

    return parsed_music

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script uses a dictionary to map the note representations to their corresponding durations. It then splits the input string into individual notes, looks up each note in the dictionary, and creates a list of the corresponding durations. The function returns this list.