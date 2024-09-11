```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.
    """
    note_map = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    music_list = music_string.split()  # split the string into a list of notes
    note_durations = [note_map[note] for note in music_list]  # get the duration of each note

    return note_durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```