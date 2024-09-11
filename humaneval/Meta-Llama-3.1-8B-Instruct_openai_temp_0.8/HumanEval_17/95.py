```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    The format is as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    note_dict = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()  # split the string into a list of notes
    beats = [note_dict[note] for note in music_list]  # create a list of beats
    return beats  # return the list of beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```