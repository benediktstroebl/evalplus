```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    result = [music_dict[note] for note in music_list]
    return result


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to the duration of each note. It uses a dictionary to map the note symbols to their durations and a list comprehension to apply this mapping to the input string. The result is then returned by the function. The script also includes a test case to demonstrate the function's usage.