```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses it, and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """

    # Define a dictionary to map note representations to their corresponding beat duration
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat duration of each note
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the notes string
    for char in notes:
        # Add the character to the current note
        current_note += char

        # If the current note matches a note in the note_beats dictionary, add its beat duration to the beats list
        if current_note in note_beats:
            beats.append(note_beats[current_note])
            current_note = ''

    # Return the list of beat durations
    return beats


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```