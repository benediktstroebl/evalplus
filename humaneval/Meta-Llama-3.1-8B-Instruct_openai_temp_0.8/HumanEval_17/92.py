```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers
    corresponding to the duration of each note in beats.

    The special ASCII format is as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
    music_string (str): A string representing musical notes in the special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the duration of each note in beats.
    """

    # Initialize an empty list to store the note durations
    note_durations = []

    # Define a dictionary to map the note strings to their corresponding durations
    note_duration_map = {
        'o': 4,
        'o|': 2,
        '|': 0,  # Added '|' to map it to 0 beats as it's a rest
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the input string
    for note in notes:
        # Check if the note is in the note duration map
        if note in note_duration_map:
            # If the note is in the map, append its duration to the list of note durations
            note_durations.append(note_duration_map[note])

    # Return the list of note durations
    return note_durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```