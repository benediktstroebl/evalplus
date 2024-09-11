```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    notes = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    return [notes[note] for note in music_list]

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes and returns a list of integers corresponding to the number of beats each note lasts. The function uses a dictionary to map the note symbols to their corresponding beat values, and then uses a list comprehension to create the output list.

When you run this script, it will print the list of integers corresponding to the number of beats each note lasts, as required by the problem.