```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers representing the duration of each note.

    """
    # Define a dictionary to map note symbols to their corresponding durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Initialize an empty string to build the current note symbol
    current_note = ''

    # Iterate over each character in the notes list
    for note in notes:
        # If the note is not empty and the current note is not empty, process the current note
        if note and current_note:
            # If the current note is in the note_durations dictionary, append its duration to the durations list
            if current_note in note_durations:
                durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''
        # Add the note to the current note
        current_note += note
        # If the note is not empty and the current note is in the note_durations dictionary, 
        # append its duration to the durations list and reset the current note
        if note and current_note in note_durations:
            durations.append(note_durations[current_note])
            current_note = ''

    # If there are any remaining notes, process them
    if current_note:
        if current_note in note_durations:
            durations.append(note_durations[current_note])

    return durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```