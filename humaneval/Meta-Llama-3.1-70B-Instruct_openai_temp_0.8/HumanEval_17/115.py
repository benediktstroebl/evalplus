```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers representing the duration of each note.

    :param music_string: A string of musical notes in ASCII format.
    :return: A list of integers representing the duration of each note.
    """

    # Define a dictionary to map each note to its corresponding duration
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # Add the duration of the current note to the list
            durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the duration of the last note to the list
    durations.append(note_durations[current_note])

    return durations


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```