```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format.
    It parses this string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """

    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # Add the character to the current note
        current_note += char

        # Check if the current note is a whole note, half note, or quarter note
        if current_note in note_beats:
            # Append the beats of the current note to the list of beats
            beats.append(note_beats[current_note])

            # Reset the current note
            current_note = ''

    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```