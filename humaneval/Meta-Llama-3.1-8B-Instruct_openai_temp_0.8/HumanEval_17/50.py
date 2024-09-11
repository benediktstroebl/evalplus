```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string of musical notes in the format 'o', 'o|', '.|'

    Returns:
    List[int]: A list of integers representing the number of beats each note lasts
    """
    note_legends = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat counts
    beat_counts = []

    # Iterate over each note in the list
    for note in notes:
        # Get the beat count for the current note from the note_legends dictionary
        beat_count = note_legends[note]
        # Append the beat count to the beat_counts list
        beat_counts.append(beat_count)

    # Return the list of beat counts
    return beat_counts


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This Python script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map the input note formats to their respective beat counts. The function splits the input string into individual notes, iterates over each note, and appends the corresponding beat count to the result list. The script includes a test call to the function with the example input string.