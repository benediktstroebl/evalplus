```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    Args:
        music_string (str): A string representing musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Create a dictionary to map the musical notes to their corresponding beats
    beats = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats
    note_beats = []

    # Iterate over each note
    for note in notes:
        # Append the beats of the current note to the list
        note_beats.append(beats.get(note, 0))  # If the note is not found in the dictionary, default to 0 beats

    # Return the list of note beats
    return note_beats


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to the beats each note lasts. The function uses a dictionary to map the musical notes to their corresponding beats, and then iterates over each note in the input string to append its beats to the output list. If a note is not found in the dictionary, it is defaulted to 0 beats. The script includes an example usage of the function.