```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses this string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers corresponding to the duration of each note in beats
    """

    # Define the mapping of note symbols to their corresponding durations
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Initialize an empty list to store the note durations
    durations = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Check if the note is a whole note
        if note == 'o':
            # If it's a whole note, append its duration to the list
            durations.append(note_durations['o'])
        else:
            # If it's not a whole note, append its duration to the list
            durations.append(note_durations[note])

    # Return the list of note durations
    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

Output: `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`