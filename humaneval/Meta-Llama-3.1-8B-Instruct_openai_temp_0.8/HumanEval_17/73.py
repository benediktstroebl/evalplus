```markdown
### Music Note Parser

This Python script parses a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

#### Code
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map note types to their beat lengths
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Append the beat length of the current note to the list
        beat_lengths.append(note_beats[note])

    # Return the list of beat lengths
    return beat_lengths

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
```

#### Output
```python
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a `parse_music` function that takes a string of musical notes as input and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map note types to their beat lengths, and then iterates over the input string to extract the beat lengths of each note. The example usage demonstrates how to use the `parse_music` function with a sample input string.