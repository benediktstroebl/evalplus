```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats does each note last.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats does each note last.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    beats = [music_dict[note] for note in music_list]
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses it, and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map the note symbols to their corresponding beat values. It then splits the input string into a list of notes, looks up each note in the dictionary, and returns the list of beat values. The script also includes a test case to demonstrate the function's behavior.