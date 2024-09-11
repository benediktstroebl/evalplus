```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes in ASCII format
    :return: A list of integers representing the number of beats each note lasts
    """

    # Define a dictionary to map note representations to their corresponding beat values
    note_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beat_values = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over the characters in the input string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its beat value to the list
            if current_note:
                beat_values.append(note_values[current_note])
                current_note = ''
        else:
            # If the character is not a space, add it to the current note
            current_note += char

    # Add the beat value of the last note to the list
    if current_note:
        beat_values.append(note_values[current_note])

    # Return the list of beat values
    return beat_values


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```