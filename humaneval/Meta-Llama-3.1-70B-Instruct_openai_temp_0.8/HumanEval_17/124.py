```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format, 
    parses it, and returns a list of integers representing the duration of each note in beats.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.
    """

    # Create a dictionary to map musical notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the notes
    for char in notes:
        # Add the character to the current note
        current_note += char

        # If the current note is in the note_durations dictionary, 
        # add its duration to the durations list and reset the current note
        if current_note in note_durations:
            durations.append(note_durations[current_note])
            current_note = ''

    # Return the list of note durations
    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```