```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    result = []

    for note in music_list:
        result.append(music_dict[note])

    return result

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

In this code, we first define a dictionary `music_dict` that maps the note symbols to their corresponding beat values. We then split the input string into a list of note symbols using the `split()` method. We iterate over each note in the list, look up its beat value in the dictionary, and append it to the `result` list. Finally, we return the `result` list.

Note that this code assumes that the input string is well-formed and contains only the specified note symbols. If the input string can contain other characters, you may need to add error handling code to handle such cases.