```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format and returns a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the number of beats for each note
    """
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is not a space, add it to the current note
        if char!='':
            note += char
        # If the character is a space, check if the current note is in the note_beats dictionary
        elif note in note_beats:
            # If it is, append its beats to the beats list
            beats.append(note_beats[note])
            # Reset the note
            note = ''
        # If the current note is not in the note_beats dictionary, it must be a whole note
        elif note == 'o':
            # Append the beats for a whole note to the beats list
            beats.append(note_beats['o'])
            # Reset the note
            note = ''

    # Check if there's a remaining note after the loop
    if note in note_beats:
        beats.append(note_beats[note])

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```