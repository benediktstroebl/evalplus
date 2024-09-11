```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Create a dictionary to map note characters to their corresponding beat durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Iterate over each note in the list of notes
    for note in notes:
        # Append the duration of the current note to the list of beat durations
        beat_durations.append(note_durations[note])

    # Return the list of beat durations
    return beat_durations


# Test the function with the provided example
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map note characters to their corresponding beat durations and then iterates over the input string, appending the duration of each note to a list. The function is then tested with the provided example.