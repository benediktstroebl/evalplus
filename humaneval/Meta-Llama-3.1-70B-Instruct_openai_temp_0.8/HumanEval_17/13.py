```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers 
    corresponding to the duration of each note in beats.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note.
    """

    # Define a dictionary to map each note to its duration
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations
    durations = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # Add the duration of the current note to the list
            durations.append(note_durations[note])
            # Reset the note
            note = ''
        else:
            # Add the character to the current note
            note += char

    # Add the duration of the last note to the list
    durations.append(note_durations[note])

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Expected output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```