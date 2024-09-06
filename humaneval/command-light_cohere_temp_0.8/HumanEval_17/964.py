Here's a self-contained Python function that takes a string of music notes in a special ASCII format, and returns a list of integers corresponding to the number of beats in the music:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string as input, representing musical notes in a special ASCII format.
    The task is to parse this string and return a list of integers corresponding to how many beats does each note last.

    Here's legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    The function uses a regular expression to split the string into individual notes, and then counts the number of occurrences to calculate the total duration of the music.

Parse Music Example:
```python
parse_music('o o| .| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
```