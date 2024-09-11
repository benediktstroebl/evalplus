```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note.
    """
    
    # Define a dictionary to map note representations to their durations
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note in the list of notes
    i = 0
    while i < len(notes):
        # Check if the current note and the next note form a single note representation
        if i + 1 < len(notes) and notes[i] + notes[i + 1] in note_durations:
            # If they do, append the duration of the combined note to the list of durations
            durations.append(note_durations[notes[i] + notes[i + 1]])
            # Skip the next note as it has already been processed
            i += 2
        elif notes[i] in note_durations:
            # If the current note is a single note representation, append its duration to the list of durations
            durations.append(note_durations[notes[i]])
            # Move on to the next note
            i += 1
        else:
            # If the current note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note: {notes[i]}")

    # Return the list of note durations
    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```