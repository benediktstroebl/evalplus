```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses the string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to the beats of each note.
    """
    
    # Define a dictionary to map note symbols to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the notes string
    for char in notes:
        # If the character is 'o' or '.', add it to the current note
        if char in ['o', '.']:
            note += char
        # If the character is '|', add it to the current note and then process the note
        elif char == '|':
            note += char
            # If the note is in the note_beats dictionary, add its beats to the beats list
            if note in note_beats:
                beats.append(note_beats[note])
            # Reset the note
            note = ''

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```