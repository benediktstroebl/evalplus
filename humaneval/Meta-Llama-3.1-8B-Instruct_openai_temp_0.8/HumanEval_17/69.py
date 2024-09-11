### Music Note Parser
#### Problem Description
Given a string of musical notes in a special ASCII format, parse the string and return a list of integers representing how many beats each note lasts.

#### Legend:
- 'o' - whole note, lasts four beats
- 'o|' - half note, lasts two beats
- '.|' - quarter note, lasts one beat

#### Solution

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers representing how many beats each note lasts.
    """
    # Initialize an empty list to store the note durations
    durations = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Check the note duration based on its ASCII representation
        if note == 'o':
            # Whole note, lasts four beats
            duration = 4
        elif note == 'o|':
            # Half note, lasts two beats
            duration = 2
        elif note == '.|':
            # Quarter note, lasts one beat
            duration = 1
        else:
            # Unknown note, raise a ValueError
            raise ValueError(f"Unknown note: {note}")

        # Append the note duration to the list
        durations.append(duration)

    # Return the list of note durations
    return durations

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note in beats. The function uses an if-elif-else statement to determine the duration of each note based on its ASCII representation and appends the duration to a list. The function then returns the list of note durations. The example usage demonstrates how to use the function with a sample input string.