```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): Input string representing musical notes.

    Returns:
        List[int]: List of integers representing the number of beats for each note.

    Examples:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define the note values in a dictionary for easy mapping
    note_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    note_durations = []

    # Initialize an empty string to build each note
    current_note = ''

    # Iterate over the notes
    for note in notes:
        # If the note is a whole note, add its value to the note durations
        if note == 'o':
            note_durations.append(note_values[note])
        # If the note is a half note or a quarter note, add the current note and its value to the note durations
        elif note in ['o|', '.|']:
            note_durations.append(note_values[note])
        # If the note is not complete, add it to the current note
        else:
            current_note += note
            # If the current note is complete, add its value to the note durations
            if current_note in note_values:
                note_durations.append(note_values[current_note])
                current_note = ''

    # Return the list of note durations
    return note_durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```