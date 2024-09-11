```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.
    
    Args:
    music_string (str): A string containing musical notes.
    
    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    note_durations = []

    # Define a dictionary to map each note to its duration
    note_legend = {
        'o': 4,  # whole note, lasts four beats
        'o|': 2,  # half note, lasts two beats
        '.|': 1  # quater note, lasts one beat
    }

    # Iterate over each note in the list of notes
    for note in notes:
        # Check if the note is in the note legend
        if note in note_legend:
            # If it is, append its duration to the note durations list
            note_durations.append(note_legend[note])
        else:
            # If it's not, raise a ValueError with a descriptive error message
            raise ValueError(f"Invalid note: '{note}'. Must be one of: {' '.join(note_legend.keys())}")

    # Return the list of note durations
    return note_durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```