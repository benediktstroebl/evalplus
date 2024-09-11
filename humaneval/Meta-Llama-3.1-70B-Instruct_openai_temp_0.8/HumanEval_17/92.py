```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses it and returns a list of integers corresponding to how many beats each note lasts.

    The legend for the notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """

    # Define a dictionary to map each note to its corresponding beats
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
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the note is not empty, add its beats to the list
            if note:
                beats.append(note_beats[note])
                note = ''
        else:
            # Add the character to the current note
            note += char

    # Add the beats for the last note
    if note:
        beats.append(note_beats[note])

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```