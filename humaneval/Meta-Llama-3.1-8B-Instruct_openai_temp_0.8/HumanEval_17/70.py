### Musical Note Parser

The following Python script defines a function `parse_music` to parse a string of musical notes in ASCII format and returns a list of integers representing the number of beats each note lasts.

```markdown
### Code
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers.
    
    The input string should contain 'o's for whole notes (4 beats), 'o|' for half notes (2 beats),
    and '.|' for quarter notes (1 beat).

    Args:
        music_string (str): A string of musical notes in ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Define a dictionary to map note characters to their respective beat lengths
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the list
    for note in notes:
        # Append the beat length of the current note to the list
        beat_lengths.append(note_beats[note])

    # Return the list of beat lengths
    return beat_lengths

### Example Usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

### Explanation

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts.

The function uses a dictionary `note_beats` to map each note character to its respective beat length. It then splits the input string into individual notes using the `split` method, and iterates over each note in the list, appending its beat length to the list.

Finally, the function returns the list of beat lengths.

The example usage demonstrates how to call the `parse_music` function with a sample input string and print the resulting list of beat lengths.