### Musical Note Parser
#### Function to parse a string of musical notes into a list of beat durations

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes into a list of beat durations.

    Args:
    - music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    - List[int]: A list of integers corresponding to how many beats each note lasts.

    Legend:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat
    """

    # Define a dictionary to map note types to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the parsed note durations
    parsed_notes = []

    # Iterate over each character in the input string
    for char in music_string:
        # Append the duration of the current note to the parsed_notes list
        parsed_notes.append(note_durations[char])

    # Return the list of parsed note durations
    return parsed_notes

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note. The function uses a dictionary to map note types to their durations, then iterates over each character in the input string to append the corresponding duration to the output list.