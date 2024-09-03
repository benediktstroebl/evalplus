```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parses the music string into a list of integers representing the number of beats.

    Legend:
    'o' - whole note, 4 beats
    'o|' - half note, 2 beats
    '.|' - quarter note, 1 beat

    Parameters:
    music_string (str): String in the special ASCII format.

    Returns:
    List[int]: List of integers corresponding to the number of beats.
    """
    music = music_string.split(' ')
    beats = []
    legend = {'o': 4, 'o|': 2, '.|': 1}

    for note in music:
        beats.append(legend[note])

    return beats
```