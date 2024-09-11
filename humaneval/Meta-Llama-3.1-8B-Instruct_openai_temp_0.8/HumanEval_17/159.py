```markdown
### Musical Note Parser

This Python script parses a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

#### Code

```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    The input string uses the following legend:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quater note, lasts one beat

    Args:
    music_string (str): A string representing musical notes in ASCII format.

    Returns:
    List[int]: A list of integers representing the number of beats each note lasts.
    """

    # Initialize an empty list to store the note durations
    note_durations = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the input string
    for note in notes:
        # Check the duration of the note based on its string representation
        if note == 'o':
            # Whole note, lasts 4 beats
            note_durations.append(4)
        elif note == 'o|':
            # Half note, lasts 2 beats
            note_durations.append(2)
        elif note == '.|':
            # Quater note, lasts 1 beat
            note_durations.append(1)

    # Return the list of note durations
    return note_durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

#### Output

```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```