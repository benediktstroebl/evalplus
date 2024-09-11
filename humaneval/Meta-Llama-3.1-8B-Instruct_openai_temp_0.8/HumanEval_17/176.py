```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    beats = {"o": 4, "o|": 2, ".|": 1}
    music_list = music_string.split()
    result = []

    for note in music_list:
        result.append(beats[note])

    return result

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format, and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map the note types to their corresponding beat values, and then splits the input string into a list of notes, appends the beat value for each note to the result list, and returns the result list.