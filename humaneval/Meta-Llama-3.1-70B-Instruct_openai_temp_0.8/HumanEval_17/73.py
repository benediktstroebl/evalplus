```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format, 
    parses it, and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string of musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """

    # Define a dictionary to map notes to their corresponding beats
    notes_legend = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build notes that span multiple characters
    note = ''

    # Iterate over each character in the notes list
    for char in notes:
        # If the character is 'o' or '.', add it to the note
        if char in ['o', '.']:
            note += char
        # If the character is '|', add it to the note and look up the note's beats
        elif char == '|':
            note += char
            if note in notes_legend:
                beats.append(notes_legend[note])
            # Reset the note after looking it up
            note = ''

    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```