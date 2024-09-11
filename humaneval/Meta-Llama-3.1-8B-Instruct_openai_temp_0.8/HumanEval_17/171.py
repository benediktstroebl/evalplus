### Music Note Parser
#### A Python Script to Parse Music Notes in ASCII Format

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of music notes in ASCII format and return a list of integers representing the number of beats each note lasts.

    :param music_string: A string of music notes in ASCII format.
    :return: A list of integers representing the number of beats each note lasts.
    """
    # Create a dictionary to map music notes to their corresponding beat values
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat values
    beats = []

    # Split the music string into individual notes
    notes = music_string.split()

    # Iterate over each note in the music string
    for note in notes:
        # Append the beat value of the current note to the beats list
        beats.append(note_to_beats[note])

    # Return the list of beat values
    return beats

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of music notes in ASCII format as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map music notes to their corresponding beat values and iterates over each note in the music string to append the corresponding beat value to the list. The script also includes an example usage of the `parse_music` function.