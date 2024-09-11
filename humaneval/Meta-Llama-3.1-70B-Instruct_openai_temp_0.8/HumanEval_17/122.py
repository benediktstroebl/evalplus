```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    Raises:
    ValueError: If an unknown note format is encountered.
    """
    # Create a dictionary mapping note formats to their corresponding beats
    note_formats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # Add the beats for the whole note to the list
            beats.append(note_formats['o'])
            # Skip the next note (the empty string)
            i += 2
        # Check if the note is a half note or a quarter note
        elif notes[i].endswith('|'):
            # Add the beats for the half or quarter note to the list
            beats.append(note_formats[notes[i]])
            i += 1
        # Check if the note is a whole note
        elif notes[i] == 'o':
            # Add the beats for the whole note to the list
            beats.append(note_formats['o'])
            i += 1
        # If the note format is unknown, raise a ValueError
        else:
            raise ValueError(f"Unknown note format: {notes[i]}")

    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```