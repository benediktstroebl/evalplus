```markdown
### Musical Note Parser
#### Parse musical notes from a string and return a list of beat durations
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes

    Returns:
        List[int]: A list of integers corresponding to the beat duration of each note

    Examples:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Create a dictionary to map note types to their beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to get the beat duration for each note
    # and convert the list of strings to a list of integers
    beat_durations = [note_durations[note] for note in notes]

    # Return the list of beat durations
    return beat_durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses the notes, and returns a list of integers corresponding to the beat duration of each note. The function uses a dictionary to map note types to their beat durations and returns a list of these durations for each note. The script also includes a test case to demonstrate the function's usage.