```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the number of beats a note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the duration of each note
    durations = []

    # Define a dictionary to map each note to its duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Iterate over each note in the list of notes
    for note in notes:
        # Check if the note is in the dictionary
        if note in note_durations:
            # If the note is in the dictionary, append its duration to the list of durations
            durations.append(note_durations[note])
        else:
            # If the note is not in the dictionary, raise a ValueError
            raise ValueError(f"Invalid note: {note}")

    # Return the list of durations
    return durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```