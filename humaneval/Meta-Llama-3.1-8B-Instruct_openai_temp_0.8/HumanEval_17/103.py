### Musical Note Parser

The following Python script defines a function to parse musical notes from a string and return a list of integers representing the duration of each note.

```markdown
### Musical Note Parser

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the duration of each note.

    Args:
    music_string (str): A string of musical notes in ASCII format.

    Returns:
    List[int]: A list of integers representing the duration of each note.
    """

    # Define a dictionary to map notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the note durations
    note_duration_list = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Append the duration of the current note to the list
        note_duration_list.append(note_durations.get(note, 0))

    # Return the list of note durations
    return note_duration_list


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note. The function uses a dictionary to map notes to their durations and iterates over the input string to append the durations to a list. The example usage at the end demonstrates how to use the function to parse a string of musical notes.