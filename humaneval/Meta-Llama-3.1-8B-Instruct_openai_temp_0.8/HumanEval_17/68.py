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

    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}  # Dictionary mapping notes to beats
    music_list = music_string.split()  # Split the input string into a list of notes
    beats_list = []  # Initialize an empty list to store the beats

    # Iterate over each note in the list and append its corresponding beats to the beats_list
    for note in music_list:
        beats_list.append(music_dict[note])

    return beats_list


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

In this script, we first define a dictionary `music_dict` that maps each musical note to its corresponding beats. We then split the input string into a list of notes using the `split()` method. We initialize an empty list `beats_list` to store the beats corresponding to each note. We iterate over each note in the list and append its corresponding beats to `beats_list` using the dictionary. Finally, we return `beats_list`.