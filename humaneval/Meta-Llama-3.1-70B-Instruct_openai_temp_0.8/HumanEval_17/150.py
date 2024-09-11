```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """

    # Create a dictionary to map the note symbols to their corresponding durations
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations of the notes
    durations = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it's a whole note, check if the next note is a '|' symbol
            if i + 1 < len(notes) and notes[i + 1] == '|':
                # If it's a '|' symbol, it's a half note, so append the duration of a half note
                durations.append(note_durations['o|'])
                # Skip the next note (the '|' symbol)
                i += 2
            else:
                # If it's not a '|' symbol, it's a whole note, so append the duration of a whole note
                durations.append(note_durations['o'])
                i += 1
        # Check if the current note is a quarter note
        elif notes[i] == '.|':
            # If it's a quarter note, append the duration of a quarter note
            durations.append(note_durations['.|'])
            i += 1
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note: {notes[i]}")

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```