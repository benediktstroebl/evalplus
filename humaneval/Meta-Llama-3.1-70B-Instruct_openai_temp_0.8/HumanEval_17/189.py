```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format.
    It parses the string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers corresponding to the beats of each note
    """

    # Create a dictionary to map the notes to their corresponding beats
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

    # Iterate over each character in the notes
    for char in notes:
        # If the character is 'o', it could be the start of a whole note or a half note
        if char == 'o':
            # Add the character to the note
            note += char
        # If the character is '|', it could be the end of a half note
        elif char == '|':
            # Add the character to the note
            note += char
            # If the note is in the note_beats dictionary, add its beats to the list
            if note in note_beats:
                beats.append(note_beats[note])
            # Reset the note
            note = ''
        # If the character is '.', it could be the start of a quarter note
        elif char == '.':
            # Add the character to the note
            note += char

    # Add the beats of the last note to the list
    if note in note_beats:
        beats.append(note_beats[note])

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```