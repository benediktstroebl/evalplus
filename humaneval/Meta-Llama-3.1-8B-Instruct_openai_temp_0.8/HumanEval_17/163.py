**Music Note Parser**
======================

Below is a Python script that defines a function to parse musical notes from a given string and return a list of integers representing the number of beats each note lasts.

```markdown
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_duration = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    parsed_notes = music_string.split()
    durations = [note_duration[note] for note in parsed_notes]

    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
```

This script defines a function `parse_music` that uses a dictionary to map each note type to its duration in beats. It then splits the input string into individual notes, looks up each note's duration in the dictionary, and returns a list of these durations. The example usage demonstrates how to call the function and print the result.