```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """Parse a string representing musical notes and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map note representations to their corresponding beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beats = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the notes
    for char in notes:
        # Add the character to the current note
        note += char

        # If the character is not a space, check if the current note is a valid note
        if note in note_beats:
            # If the note is valid, append its beat value to the beats list and reset the note
            beats.append(note_beats[note])
            note = ''

    # Return the list of beat values
    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```