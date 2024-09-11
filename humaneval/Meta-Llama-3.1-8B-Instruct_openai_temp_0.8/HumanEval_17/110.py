```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format, 
    parses the string, and returns a list of integers representing how many beats each note lasts.

    The notes and their corresponding beat lengths are:
    - 'o' - whole note, lasts 4 beats
    - 'o|' - half note, lasts 2 beats
    - '.|' - quarter note, lasts 1 beat

    Args:
        music_string (str): A string representing musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers representing how many beats each note lasts.
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}
    parsed_music = music_string.split()
    result = [music_dict[note] for note in parsed_music]
    return result


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes in a special ASCII format, 
parses the string, and returns a list of integers representing how many beats each note lasts.
It uses a dictionary to map the note characters to their corresponding beat lengths.
The function splits the input string into a list of notes, looks up the beat length for each note in the dictionary, 
and returns the list of beat lengths.
Finally, the script tests the function with the provided example input.