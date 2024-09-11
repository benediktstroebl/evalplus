### Parsing Musical Notes

Below is a Python script that solves the problem of parsing musical notes from a given string.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers representing the number of beats each note lasts.

    Example:
    >>> parse_music('o o|.* o| o|.*.*.*.* o o')
    [4, 4, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    result = []
    music_string +=''  # Add a space at the end of the string
    for i in range(len(music_string)):
        if music_string[i] in notes:
            result.append(notes[music_string[i:i+2]])
            i += 1  # Skip the next character
    return result

# Test the function
print(parse_music('o o|.* o| o|.*.*.*.* o o'))
```

This script defines a function `parse_music` that takes a string `music_string` as input and returns a list of integers representing the number of beats each note lasts. It uses a dictionary `notes` to map each note type to its corresponding number of beats. The function then iterates over the input string, and whenever it encounters a valid note, it appends the corresponding number of beats to the result list. Finally, the script tests the function with a sample input string.