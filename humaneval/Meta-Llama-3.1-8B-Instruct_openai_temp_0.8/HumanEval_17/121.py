```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats for each note.

    Args:
        music_string (str): A string of musical notes in the format 'o', 'o|', '.|'.

    Returns:
        List[int]: A list of integers representing the number of beats for each note.

    Notes:
        'o' - whole note, lasts four beats
        'o|' - half note, lasts two beats
        '.|' - quarter note, lasts one beat
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    beat_list = [music_dict[note] for note in music_list]
    return beat_list

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script uses a dictionary to map the note formats to their corresponding beat counts, then splits the input string into a list of notes and uses a list comprehension to replace each note with its corresponding beat count. The resulting list of beat counts is then returned.