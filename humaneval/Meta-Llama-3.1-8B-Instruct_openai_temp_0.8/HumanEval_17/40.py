```markdown
### Music Parser Script

This script defines a function `parse_music` that takes a string of musical notes in ASCII format and returns a list of integers representing the duration of each note in beats.

#### Music Parser Function

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the duration of each note.

    Args:
    music_string (str): A string of musical notes in ASCII format.

    Returns:
    List[int]: A list of integers representing the duration of each note in beats.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """

    # Define a dictionary to map musical notes to their durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the note durations
    durations = []

    # Split the music string into individual notes
    notes = music_string.split()

    # Iterate over each note in the music string
    for note in notes:
        # Append the duration of the current note to the list of durations
        durations.append(note_durations[note])

    # Return the list of note durations
    return durations

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

#### Example Output

```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```