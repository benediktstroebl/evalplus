```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers representing the number of beats each note lasts.

    The legend is as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string of musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    notes = {'o': 4, 'o|': 2, '.|': 1}  # Dictionary to map notes to their corresponding beats
    return [notes[note] for note in music_string.split()]  # Split the string by space and map each note to its beats


# Example usage:
music_notes = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_notes))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```