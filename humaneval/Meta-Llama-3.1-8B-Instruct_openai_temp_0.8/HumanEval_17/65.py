```markdown
### Music Note Parser
#### Parse musical notes from a string and return a list of integers representing the note durations

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the note durations.

    Args:
        music_string (str): A string of musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers representing the note durations.
    """
    # Define a dictionary to map musical notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note in the notes list
    for note in notes:
        # Append the duration of the current note to the durations list
        durations.append(note_durations[note])

    # Return the list of note durations
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the note durations. The function uses a dictionary to map musical notes to their durations and then splits the input string into individual notes before iterating over each note to append its duration to the list. The script includes a test case to demonstrate the function's usage.