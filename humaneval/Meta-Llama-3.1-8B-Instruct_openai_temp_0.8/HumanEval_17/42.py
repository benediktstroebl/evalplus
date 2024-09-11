### Music Note Parser
#### Problem Statement
Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the duration of each note.

#### Legend
* `'o'` - whole note, lasts four beats
* `'o|'` - half note, lasts two beats
* `'.|'` - quarter note, lasts one beat

#### Solution

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the duration of each note.

    Args:
        music_string (str): A string representing musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the duration of each note.
    """
    # Define a dictionary to map note symbols to their durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to extract the durations of each note
    durations = [note_durations[note] for note in notes]

    return durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to the duration of each note. The function uses a dictionary to map note symbols to their durations and a list comprehension to extract the durations of each note. The example usage at the end demonstrates how to call the function with a sample input string.