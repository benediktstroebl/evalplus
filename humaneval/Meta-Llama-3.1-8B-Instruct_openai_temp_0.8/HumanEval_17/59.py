```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in ASCII format and returns a list of integers representing the number of beats each note lasts.

    Args:
        music_string (str): A string of musical notes in ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """

    # Dictionary to map note types to their beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Iterate over each note in the notes list
    for note in notes:
        # Append the beat duration of the current note to the beat_durations list
        beat_durations.append(note_durations.get(note, 0))

    # Return the list of beat durations
    return beat_durations


# Test the function
if __name__ == "__main__":
    music_string = 'o o|.| o| o|.|.|.|.| o o'
    print(parse_music(music_string))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map note types to their beat durations and then splits the input string into individual notes to calculate their beat durations. The script also includes a test case to verify the function's correctness.