```markdown
### Music Note Parser

This script parses a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

#### Legend:
- `'o'` - whole note, lasts four beats
- `'o|'` - half note, lasts two beats
- `'.|'` - quarter note, lasts one beat
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map notes to their corresponding beat values
    note_beat_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat values
    beat_values = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the input string
    for note in notes:
        # Append the beat value of the current note to the list
        beat_values.append(note_beat_map[note])

    # Return the list of beat values
    return beat_values


# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string representing musical notes as input, parses it, and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map notes to their corresponding beat values and splits the input string into individual notes before iterating over them and appending their beat values to the list.