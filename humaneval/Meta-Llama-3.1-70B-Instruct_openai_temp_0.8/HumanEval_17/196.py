```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    """
    # Create a dictionary to map musical notes to their corresponding beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of musical notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note in the list of notes
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it is, append its beats to the list and move to the next note
            beats.append(note_to_beats['o'])
            i += 1
        # Check if the current note is a half note or a quarter note
        elif i < len(notes) - 1 and notes[i] + notes[i + 1] in note_to_beats:
            # If it is, append its beats to the list and move to the next two notes
            beats.append(note_to_beats[notes[i] + notes[i + 1]])
            i += 2
        else:
            # If the current note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note: {notes[i]}")

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```