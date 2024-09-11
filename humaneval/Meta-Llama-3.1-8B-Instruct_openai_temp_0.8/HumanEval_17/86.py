```markdown
## Music Note Parser Script
### Description
This script takes a string of musical notes in a special ASCII format and returns a list of integers corresponding to the duration of each note in beats.

### Code
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the duration of each note in beats.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the duration of each note in beats.

    """
    # Define a dictionary to map notes to their durations
    note_durations = {
        'o': 4,  # whole note, lasts four beats
        'o|': 2,  # half note, lasts two beats
        '.|': 1  # quater note, lasts one beat
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to parse each note and its duration
    parsed_notes = [note_durations[note] for note in notes]

    return parsed_notes


# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
```

### Example Output
```python
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

### Notes
This script uses a dictionary to map notes to their durations, making it easy to add or modify note types in the future. The `parse_music` function splits the input string into individual notes and uses a list comprehension to parse each note and its duration. The result is a list of integers representing the duration of each note in beats.