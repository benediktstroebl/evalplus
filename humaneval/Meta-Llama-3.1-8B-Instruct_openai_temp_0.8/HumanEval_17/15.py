```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers corresponding to how many beats each note lasts.

    The input string uses a special ASCII format:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    beats = [music_dict[note] for note in music_list]
    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

In this script, the `parse_music` function takes a string of musical notes as input, splits it into individual notes, looks up the note in a dictionary to determine its beat length, and returns a list of the beat lengths. The dictionary `music_dict` maps each note to its corresponding beat length, and the list comprehension `[music_dict[note] for note in music_list]` uses this dictionary to create the list of beat lengths.