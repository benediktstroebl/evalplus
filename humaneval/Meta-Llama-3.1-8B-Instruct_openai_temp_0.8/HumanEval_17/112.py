```markdown
### Music Note Parsing Script

This script takes a string of musical notes in a special ASCII format and returns a list of integers
representing how many beats each note lasts.

#### Code
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats does each note last.

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map notes to their corresponding beat lengths
    note_to_beat = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Iterate over each note in the list of notes
    for note in notes:
        # Append the beat length of the note to the list of beat lengths
        beat_lengths.append(note_to_beat[note])

    # Return the list of beat lengths
    return beat_lengths


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

#### Explanation

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing how many beats each note lasts.

The function first defines a dictionary `note_to_beat` to map each note to its corresponding beat length. It then splits the input string into individual notes using the `split` method. Finally, it iterates over each note in the list of notes and appends its beat length to the list of beat lengths.

The script includes an example usage of the `parse_music` function at the end, which demonstrates how to call the function with a sample input string and print the resulting list of beat lengths.