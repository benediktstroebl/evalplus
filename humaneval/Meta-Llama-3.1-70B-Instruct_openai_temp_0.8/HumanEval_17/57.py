```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer corresponds to how many beats each note lasts.

    :param music_string: A string of musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """

    # Define a dictionary to map each note to its corresponding duration
    note_durations = {
        'o': 4,  # Whole note
        'o|': 2,  # Half note
        '.|': 1  # Quarter note
    }

    # Initialize an empty list to store the durations
    durations = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the note is not empty, add its duration to the list
            if note:
                durations.append(note_durations[note])
                note = ''
        else:
            # If the character is not a space, add it to the current note
            note += char

    # After the loop, there might be a note left over that was not followed by a space
    # So, add its duration to the list if it's not empty
    if note:
        durations.append(note_durations[note])

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```