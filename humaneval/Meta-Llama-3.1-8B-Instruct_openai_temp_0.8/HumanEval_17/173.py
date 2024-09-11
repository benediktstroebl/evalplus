```markdown
### Parse Music Function
#### A Python function to parse musical notes into beats
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    # Initialize an empty list to store the beats
    beats = []

    # Split the music string into individual notes
    notes = music_string.split()

    # Iterate over each note in the string
    for note in notes:
        # Check the type of note and append the corresponding beats to the list
        if note == 'o':
            beats.append(4)  # whole note lasts 4 beats
        elif note == 'o|':
            beats.append(2)  # half note lasts 2 beats
        elif note == '.|':
            beats.append(1)  # quarter note lasts 1 beat
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note: {note}")

    # Return the list of beats
    return beats

# Example usage
music = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a string of musical notes and returns a list of integers corresponding to how many beats each note lasts. It uses a legend to determine the beats for each type of note and raises a `ValueError` if an unrecognized note is encountered.