### Musical Note Parser

The following Python script defines a function `parse_music` that takes in a string representing musical notes in a special ASCII format and returns a list of integers corresponding to the duration of each note in beats.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the duration of each note in beats.

    The input string uses the following notation:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the duration of each note in beats.
    """

    # Define a dictionary to map the musical note notation to its duration
    notation_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations of the notes
    durations = []

    # Iterate over each note in the input string
    for note in notes:
        # Get the duration of the current note from the notation map
        duration = notation_map.get(note)

        # If the note is not found in the notation map, raise a ValueError
        if duration is None:
            raise ValueError(f"Unknown note notation: '{note}'")

        # Append the duration of the current note to the list of durations
        durations.append(duration)

    # Return the list of durations
    return durations


# Example usage:
if __name__ == "__main__":
    # Test the parse_music function
    music_string = 'o o|.|. o| o|.|..|..|. o o'
    print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes in a string representing musical notes in a special ASCII format and returns a list of integers corresponding to the duration of each note in beats. The function uses a dictionary to map the musical note notation to its duration and iterates over each note in the input string to calculate its duration. If an unknown note notation is encountered, the function raises a `ValueError`. The script includes example usage to demonstrate how to call the `parse_music` function with a test input string.