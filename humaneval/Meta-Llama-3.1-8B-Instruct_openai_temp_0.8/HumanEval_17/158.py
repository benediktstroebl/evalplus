```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers where each integer corresponds to the number of beats a note lasts.

    Notes:
        The legend for the notes is:
        'o' - whole note, lasts four beats
        'o|' - half note, lasts two beats
        '.|' - quarter note, lasts one beat
    """
    # Create a dictionary to map each note to its duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the results
    results = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Append the duration of the note to the results list
        results.append(note_durations[note])

    # Return the list of results
    return results


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines the `parse_music` function, which takes a string of musical notes and returns a list of integers representing the duration of each note. It uses a dictionary to map each note to its duration and splits the input string into individual notes to process them separately.