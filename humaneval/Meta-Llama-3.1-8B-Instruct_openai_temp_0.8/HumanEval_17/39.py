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
        List[int]: A list of integers corresponding to how many beats each note lasts
    """

    # Create a dictionary to map note types to their corresponding beat lengths
    note_types = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Iterate over each note
    for note in notes:
        # Append the beat length of the current note to the list
        beat_lengths.append(note_types[note])

    # Return the list of beat lengths
    return beat_lengths


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```