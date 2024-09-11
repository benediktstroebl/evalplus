### Parse Musical Notes from String
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    The legend is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Define a dictionary mapping notes to their beat values
    note_to_beats = {
        'o': 4,
        'o|': 2,
        'o.': 1,
        '.': 1,
        '.|': 1,
        'o|o': 2,
        'o.o': 1,
        'o.o|': 1,
        '.|o':1,
        '.|.|': 1,
        'o|o|': 2,
        'o.o|': 1,
        'o.o.o|': 1,
        '.|.o': 1,
        '.|.o|': 1,
        '.|.o.o|': 1,
        '.|.|o':1,
        '.|.|o|': 2,
        '.|.|o.o|': 1
    }

    # Split the input string into notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beat_values = []

    # Iterate over each note in the input string
    for note in notes:
        # Append the beat value of the current note to the list
        beat_values.append(note_to_beats.get(note, 0))

    # Return the list of beat values
    return beat_values

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This Python script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts. The script then tests this function with the example input provided. The function works by splitting the input string into individual notes, looking up the beat value of each note in a dictionary, and appending this value to a list. The script includes a test case at the end to verify that the function works correctly.