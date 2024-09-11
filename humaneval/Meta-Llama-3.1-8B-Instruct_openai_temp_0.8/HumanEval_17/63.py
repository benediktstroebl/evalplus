```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map the legend to beat counts
    note_legend = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat counts
    beat_counts = []

    # Iterate over each note in the notes list
    for note in notes:
        # Append the beat count of the current note to the beat_counts list
        beat_counts.append(note_legend[note])

    # Return the list of beat counts
    return beat_counts

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script first defines a dictionary `note_legend` to map the legend to beat counts. It then splits the `music_string` into individual notes using the `split()` method and initializes an empty list `beat_counts` to store the beat counts. Finally, it iterates over each note in the `notes` list, appends the beat count of the current note to the `beat_counts` list, and returns the list of beat counts. The test case at the end checks the function with the given example.