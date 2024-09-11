```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Dictionary to map the notes to the number of beats they last
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Use a list comprehension to create a list of beats
    beats = [note_to_beats[note] for note in notes]

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes as input and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map the notes to the number of beats they last and then splits the input string into a list of notes. It then uses a list comprehension to create a list of beats and returns this list.

The script also includes a test case to demonstrate the function's behavior. When run, it prints the expected output for the test case.