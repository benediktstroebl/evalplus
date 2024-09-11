```markdown
### Music Note Parser
#### Problem Description
Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

#### Legend
- 'o' - whole note, lasts four beats
- 'o|' - half note, lasts two beats
- '.|' - quarter note, lasts one beat

#### Solution
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Check the note type and append its beat length to the list
        if note == 'o':
            beat_lengths.append(4)  # whole note lasts four beats
        elif note == 'o|':
            beat_lengths.append(2)  # half note lasts two beats
        elif note == '.|':
            beat_lengths.append(1)  # quarter note lasts one beat

    # Return the list of beat lengths
    return beat_lengths

# Test the function
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to how many beats each note lasts. It uses a dictionary to map note types to their beat lengths, then splits the input string into individual notes, iterates over each note, and appends its beat length to the list. Finally, it returns the list of beat lengths.