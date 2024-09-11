### Music Note Parser
#### A Python script to parse musical notes in ASCII format and return their corresponding beat durations.

```markdown
### Code

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers corresponding to the duration of each note.

    Notes:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the duration of each note.
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}  # Dictionary mapping notes to their durations
    notes = music_string.split()  # Split the input string into individual notes
    note_durations = []  # Initialize a list to store the note durations

    for note in notes:
        note_durations.append(music_dict[note])  # Append the duration of each note to the list

    return note_durations  # Return the list of note durations

### Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

### Explanation

This script defines a function `parse_music` that takes a string of musical notes in ASCII format as input. The function uses a dictionary `music_dict` to map each note to its corresponding duration. It then splits the input string into individual notes and appends their durations to a list `note_durations`. Finally, the function returns the list of note durations.

The script also includes a test case that prints the durations of a given musical note sequence.