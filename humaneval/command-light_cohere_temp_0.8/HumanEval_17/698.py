```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here's legend:
        'o' - whole note, lasts four beats
        'o|' - half note, lasts two beats
        '.|' - quarter note, lasts one beat

    >>> return [int(x) for x in music_string.split('o bando string is: 'o o| .| o| .| .| .| .| o o')]
    """
    return [int(x) for x in music_string.split(' band')]
```