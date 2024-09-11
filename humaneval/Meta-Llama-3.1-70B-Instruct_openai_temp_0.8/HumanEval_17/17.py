```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes in a special ASCII format.
    :return: A list of integers representing the number of beats each note lasts.
    """

    # First, we split the input string into individual notes
    notes = music_string.split()

    # Then, we use a dictionary to map each note to its corresponding number of beats
    note_to_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Finally, we use a list comprehension to convert each note to its corresponding number of beats
    beats = [note_to_beats[note] for note in notes]

    return beats

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```