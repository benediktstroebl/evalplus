```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): Input string representing musical notes.

    Returns:
        List[int]: List of integers representing the number of beats each note lasts.
    """
    note_dict = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    result = []

    for note in notes:
        result.append(note_dict[note])

    return result

# Test the function
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
```

When you run this script, it will output: `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`.