```markdown
### Music Note Parser
#### Parses a string of musical notes and returns a list of integers representing note durations.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): String representing musical notes in ASCII format.

    Returns:
        List[int]: List of integers representing note durations.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store note durations
    durations = []

    # Iterate over each note
    for note in notes:
        # Get the note duration from the dictionary
        duration = note_durations.get(note)

        # If the note duration is found, append it to the list
        if duration is not None:
            durations.append(duration)

    # Return the list of note durations
    return durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, splits it into individual notes, looks up their durations in a dictionary, and returns a list of these durations. It includes a legend explaining the note durations, an example usage, and proper docstrings for the function.