```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the number of beats each note lasts.
    """
    # Define a dictionary to map each note to its corresponding beat duration
    note_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to look up the beat duration for each note and return the results
    return [note_map[note] for note in notes]

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a string of musical notes as input, splits it into individual notes, and looks up each note's beat duration in a dictionary. The results are returned as a list of integers. The example usage at the end demonstrates how to call the function and print the result.