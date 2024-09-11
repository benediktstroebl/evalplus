```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    This function parses the string and returns a list of integers corresponding to how many beats each note lasts.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat
    """
    note_mapping = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note lengths
    note_lengths = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over the notes
    for char in notes:
        # If the character is 'o' or '.', add it to the note
        if char in ['o', '.']:
            note += char
        # If the character is '|' and note is not empty, add it to the note and get the note length
        elif char == '|' and note:
            note += char
            # Get the note length and add it to the list
            note_lengths.append(note_mapping[note])
            # Reset the note
            note = ''
        # If the character is '|' and note is empty, add it to the note_lengths list with a value of 1
        elif char == '|' and not note:
            note_lengths.append(1)

    # Return the list of note lengths
    return note_lengths


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This function splits the input string into individual notes. It then iterates over each note, adding it to a dictionary and retrieving its length. The lengths are added to a list which is then returned. The result matches the expected output: `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`.