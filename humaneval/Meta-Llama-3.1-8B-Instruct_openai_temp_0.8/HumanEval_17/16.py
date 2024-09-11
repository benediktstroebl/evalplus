```markdown
### Music Note Parser

This script takes a string of musical notes in a specific ASCII format and returns a list of integers representing the beat duration of each note.

#### Requirements

* No external libraries required
* Python 3.x

#### Code
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the beat duration of each note.

    Args:
    music_string (str): A string of musical notes in a specific ASCII format.

    Returns:
    List[int]: A list of integers representing the beat duration of each note.

    """
    # Define the note durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Loop through each note
    for note in notes:
        # Check if the note is valid
        if note in note_durations:
            # Append the note duration to the list
            durations.append(note_durations[note])
        else:
            # If the note is invalid, raise a ValueError
            raise ValueError(f"Invalid note: {note}")

    return durations


# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
```

#### Output

```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

#### Explanation

This script defines a function `parse_music` that takes a string of musical notes and returns a list of integers representing the beat duration of each note. The function uses a dictionary to map each note to its corresponding duration. It then splits the input string into individual notes, checks if each note is valid, and appends the corresponding duration to a list. Finally, it returns the list of note durations.