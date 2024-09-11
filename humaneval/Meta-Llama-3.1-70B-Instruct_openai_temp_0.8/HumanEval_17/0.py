```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """

    # Create a dictionary to map each note to its duration in beats
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the duration of each note
    durations = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o':
            # If the note is a whole note, append its duration to the list
            durations.append(note_durations['o'])
        # Check if the note is a half note or a quarter note
        elif i < len(notes) - 1 and notes[i] + notes[i + 1] in note_durations:
            # If the note is a half note or a quarter note, append its duration to the list
            durations.append(note_durations[notes[i] + notes[i + 1]])
            # Skip the next note as it has already been processed
            i += 1
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Invalid note: {notes[i]}")
        i += 1

    # Return the list of note durations
    return durations


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```