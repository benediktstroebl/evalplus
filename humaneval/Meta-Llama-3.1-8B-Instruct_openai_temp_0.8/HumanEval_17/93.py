### Music Parser Script
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format
    :return: A list of integers corresponding to how many beats each note lasts
    """
    notes = music_string.split()
    beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Use a list comprehension to create a list of beat lengths
    return [beats[note] for note in notes]


# Example usage:
music_string = 'o o|.* o| o|.*.*.*.* o o'
print(parse_music(music_string))
```
This script defines a function `parse_music` that takes a string of musical notes, splits it into individual notes, looks up the beat length for each note in a dictionary, and returns a list of beat lengths. The example usage at the end demonstrates how to use this function to parse a string of musical notes and print the resulting list of beat lengths.