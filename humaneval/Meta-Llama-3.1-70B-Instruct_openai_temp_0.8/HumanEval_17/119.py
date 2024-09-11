```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format, 
    parses it, and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.
    """

    # Define a dictionary to map each note type to its corresponding duration
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # Append the whole note duration to the list
            durations.append(note_durations['o'])
            # Move to the next note
            i += 1
        # Check if the current note is a half note or a quarter note
        elif notes[i] + '|' in note_durations:
            # Append the half or quarter note duration to the list
            durations.append(note_durations[notes[i] + '|'])
            # Skip the '|' character and move to the next note
            i += 2

    # Return the list of note durations
    return durations


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```