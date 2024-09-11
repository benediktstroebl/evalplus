```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to look up each note in the dictionary and append its corresponding beats
    beats = [note_beats[note] for note in notes]

    return beats


# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script first defines a dictionary to map notes to their corresponding beats. It then splits the input string into individual notes, looks up each note in the dictionary, and appends its corresponding beats to a list. Finally, it returns the list of beats. The example usage at the end shows how to use the function with a sample input string.