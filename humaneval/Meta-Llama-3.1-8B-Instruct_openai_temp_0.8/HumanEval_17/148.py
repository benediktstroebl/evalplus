```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    This function parses the input string and returns a list of integers corresponding to how many beats each note lasts.

    The legend for the notes is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    beats_per_note = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    parsed_music = [beats_per_note[note] for note in music_list]
    return parsed_music

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map each note to its corresponding beat count, then splits the input string into individual notes and uses a list comprehension to create the output list. Finally, the script tests the function with the provided example input.