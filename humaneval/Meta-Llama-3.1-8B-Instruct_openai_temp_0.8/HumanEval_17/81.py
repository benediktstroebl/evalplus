### Music Note Parser
#### Python Script
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the duration of each note.

    Args:
    music_string (str): A string of musical notes in the format 'o', 'o|', or '.|'.

    Returns:
    List[int]: A list of integers representing the duration of each note in beats.
    """
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note in the input string
    for note in notes:
        # Append the duration of the current note to the list of durations
        durations.append(note_durations[note])

    # Return the list of durations
    return durations

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script uses a dictionary to map each musical note to its corresponding duration in beats. It then splits the input string into individual notes and appends the duration of each note to a list. Finally, it returns the list of durations.