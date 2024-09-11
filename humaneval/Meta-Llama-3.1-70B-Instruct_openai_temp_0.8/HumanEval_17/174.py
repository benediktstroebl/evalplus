```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map musical notes to their corresponding beat duration
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat duration of each note
    beats = []

    # Initialize an empty string to build notes with multiple characters
    note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char.isspace():
            # If the note is not empty, add its beat duration to the list
            if note:
                beats.append(note_beats[note])
                note = ''
        else:
            # If the character is not a space, add it to the current note
            note += char
            # If the current note is in the note_beats dictionary, add its beat duration to the list
            if note in note_beats:
                beats.append(note_beats[note])
                note = ''

    # Return the list of beat durations
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```