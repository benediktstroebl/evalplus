Here's a self-contained Python script that solves the problem:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string of musical notes in the specified format.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.
    """

    # Define a dictionary to map the note patterns to their corresponding durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations
    durations = []

    # Iterate over each note in the list
    for note in notes:
        # Append the duration of the current note to the list
        durations.append(note_durations[note])

    # Return the list of durations
    return durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses it into individual notes, looks up their durations in a dictionary, and returns a list of these durations. The function uses a dictionary to map note patterns to their corresponding durations, and it splits the input string into individual notes using the `split` method. The script also includes an example usage at the end to demonstrate how to use the `parse_music` function.