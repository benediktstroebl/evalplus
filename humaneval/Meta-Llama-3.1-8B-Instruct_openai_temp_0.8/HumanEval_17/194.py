```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string of ASCII musical notes.

    Returns:
    List[int]: A list of integers where each integer represents the number of beats a note lasts.

    """
    # Create a dictionary to map special characters to their corresponding values
    note_values = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the parsed note values
    parsed_notes = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note and append its value to the parsed_notes list
    for note in notes:
        # Check if the note is a valid character
        if note in note_values:
            # Append the value of the note to the parsed_notes list
            parsed_notes.append(note_values[note])
        else:
            # If the note is not valid, raise a ValueError
            raise ValueError(f"Invalid note: {note}")

    # Return the parsed_notes list
    return parsed_notes

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses the string, and returns a list of integers corresponding to the number of beats each note lasts. It uses a dictionary to map special characters to their corresponding values and iterates over each note in the input string to append its value to a list.