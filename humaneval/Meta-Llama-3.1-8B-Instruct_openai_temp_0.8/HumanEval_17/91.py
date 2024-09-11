```markdown
### Music Note Parser
#### Python Script to Parse Musical Notes from ASCII Format

```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers representing the number of beats each note lasts.

    Legend:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string of musical notes in ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """

    # Define a dictionary to map note types to their corresponding beat values
    note_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the parsed note values
    parsed_notes = []

    # Iterate over each character in the input string
    for char in music_string:
        # Check if the character is in the note values dictionary
        if char in note_values:
            # Append the corresponding note value to the parsed notes list
            parsed_notes.append(note_values[char])
        else:
            # If the character is not a valid note, raise a ValueError
            raise ValueError(f"Invalid note: {char}")

    # Return the list of parsed note values
    return parsed_notes


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes in ASCII format as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map note types to their corresponding beat values and iterates over each character in the input string to parse the notes. If an invalid note is encountered, a ValueError is raised. The example usage demonstrates how to call the function with a sample input string and print the resulting list of parsed note values.