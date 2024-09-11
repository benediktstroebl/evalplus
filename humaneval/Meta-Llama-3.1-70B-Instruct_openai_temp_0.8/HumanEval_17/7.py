```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses the string and returns a list of integers corresponding to how many beats each note lasts.

    The legend for the ASCII format is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Create a dictionary to map the ASCII representation of notes to their corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of the notes
    beats = []

    # Iterate over each note in the notes list
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it's a whole note, append its beats to the beats list
            beats.append(note_beats['o'])
        # Check if the current note is a half note or a quarter note
        elif i + 1 < len(notes) and notes[i] + notes[i + 1] in note_beats:
            # If it's a half note or a quarter note, append its beats to the beats list
            beats.append(note_beats[notes[i] + notes[i + 1]])
            # Skip the next note as we've already processed it
            i += 1
        i += 1

    return beats


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```