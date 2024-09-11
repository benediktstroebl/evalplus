```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers representing the beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in the format 'o', 'o|', or '.|'.

    Returns:
        List[int]: A list of integers representing the beats each note lasts.
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}
    beats = [value for char in music_string.split() for value in (music_dict.get(char, 0),)]
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the beats each note lasts. The function uses a dictionary to map the musical notes to their corresponding beat values, then uses a list comprehension to split the input string into individual notes and look up their beat values in the dictionary. The function is then tested with the provided example string.