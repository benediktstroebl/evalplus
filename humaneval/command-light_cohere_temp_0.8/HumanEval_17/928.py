Here is a Python script that includes the function `parse_music`, which is designed to parse a string of musical notes and return a list of corresponding beat counts:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to how many beats does each last.

    Here is legend:
    - 'o' - whole note, lasts 4 beats
    - 'o|' - half note, lasts 2 beats
    - '.' - quarter note, lasts 1 beat

    Args:
        music_string (str): A string of musical notes in the format 'note rest note rest ...'.

    Returns:
        List[int]: A list of integers representing the beat count for each note.
    """

    example:
    music_string = 'o o| .| o| .| .| .| .| o o'
    beats = parse_music(music_string)
    assert beats == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```