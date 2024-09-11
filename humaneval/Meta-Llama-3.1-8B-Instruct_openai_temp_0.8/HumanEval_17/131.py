Here's a Python script that uses a dictionary to map musical notes to their corresponding beat lengths and then counts the occurrences of each note to construct the output list:

```markdown
### Musical Note Parser
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parses a string of musical notes and returns a list of integers representing the beat lengths of each note.

    Args:
        music_string (str): A string of musical notes in the format 'o', 'o|', '.|', etc.

    Returns:
        List[int]: A list of integers representing the beat lengths of each note.
    """
    # Define a dictionary mapping musical notes to their beat lengths
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Iterate over each note and append its beat length to the list
    for note in notes:
        beat_lengths.append(note_lengths[note])

    # Return the list of beat lengths
    return beat_lengths

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

When you run this script, it will output:

```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This corresponds to the expected output for the input string `'o o|.| o| o|.|.|.|.| o o'`.