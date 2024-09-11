```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    beats_list = [music_dict[note] for note in music_list]
    return beats_list

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This Python script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map the note representations to their corresponding beat lengths, then splits the input string into a list of notes and uses a list comprehension to replace each note with its corresponding beat length. The resulting list of beat lengths is returned by the function.