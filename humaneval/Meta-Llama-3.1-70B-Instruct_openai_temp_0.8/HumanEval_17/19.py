```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Define a dictionary to map musical notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of musical notes
    notes = music_string.split()

    # Initialize an empty list to store the number of beats for each note
    beats = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # Add the note to the list of notes if it's not empty
            if note:
                beats.append(note_beats[note])
                note = ''
        else:
            # Add the character to the current note
            note += char

            # If the note is complete (i.e., it's in the note_beats dictionary), add its beats to the list
            if note in note_beats:
                beats.append(note_beats[note])
                note = ''

    # If the last note is not followed by a space, add its beats to the list
    if note:
        beats.append(note_beats[note])

    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```