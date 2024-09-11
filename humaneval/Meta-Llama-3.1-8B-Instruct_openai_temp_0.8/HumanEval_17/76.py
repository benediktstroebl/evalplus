### Musical Note Parser
#### A Python Script to Parse Musical Notes in ASCII Format

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in ASCII format and return a list of integers
    corresponding to the number of beats each note lasts.

    :param music_string: A string representing musical notes in ASCII format.
    :return: A list of integers representing the number of beats each note lasts.
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}  # Create a dictionary to map notes to beat duration
    music_list = music_string.split()  # Split the input string into a list of notes
    parsed_music = []  # Initialize an empty list to store the parsed music

    for note in music_list:  # Iterate over each note in the list
        parsed_music.append(music_dict[note])  # Append the beat duration of the note to the parsed music list

    return parsed_music  # Return the parsed music list

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes in ASCII format as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map musical notes to their corresponding beat durations and a list comprehension to parse the input string. The example usage demonstrates how to use the `parse_music` function with a sample music string.