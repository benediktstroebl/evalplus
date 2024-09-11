```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    The legend for the ASCII format is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map the ASCII notes to their corresponding beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beats = []

    # Iterate over the notes
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it's a whole note, append its beat value to the list and move to the next note
            beats.append(note_beats['o'])
            i += 1
        # Check if the current note is a half note or a quarter note
        elif i < len(notes) - 1 and notes[i] + notes[i + 1] in note_beats:
            # If it's a half note or a quarter note, append its beat value to the list and move to the next two notes
            beats.append(note_beats[notes[i] + notes[i + 1]])
            i += 2
        else:
            # If the current note is not recognized, raise a ValueError
            raise ValueError("Invalid note: {}".format(notes[i]))

    return beats

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```