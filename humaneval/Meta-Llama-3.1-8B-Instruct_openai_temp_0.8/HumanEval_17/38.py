### Musical Note Parser Script
```markdown
### Musical Note Parser
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers
    corresponding to the number of beats each note lasts.

    :param music_string: A string of musical notes in the format:
        'o' - whole note (4 beats)
        'o|' - half note (2 beats)
        '.|' - quarter note (1 beat)
    :return: A list of integers representing the number of beats each note lasts
    """
    # Define a dictionary to map note types to their corresponding beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the string
    for note in notes:
        # Append the beat length of the current note to the list
        beat_lengths.append(note_beats[note])

    # Return the list of beat lengths
    return beat_lengths

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses it according to the specified format, and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map note types to their corresponding beat lengths, making it easy to add or remove note types in the future. The example usage at the end demonstrates how to use the function with a sample input string.