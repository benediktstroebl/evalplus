```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    'o' - whole note, lasts four beats

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Create a dictionary to map the notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the note durations
    durations = []

    # Split the input string into notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Append the duration of the note to the list
        durations.append(note_durations[note])

    # Return the list of note durations
    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts. It uses a dictionary to map the notes to their durations and splits the input string into individual notes to determine their durations. The script then prints the result of calling `parse_music` with the test string.