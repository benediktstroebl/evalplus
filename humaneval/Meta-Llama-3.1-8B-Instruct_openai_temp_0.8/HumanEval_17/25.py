```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = []
    for note in music_string.split():
        beats.append(notes.get(note, 0))
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts. It then tests the function with the provided example.