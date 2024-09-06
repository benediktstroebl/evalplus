```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is the legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    >>> return [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    notes = [beat for beat in map(lambda x: x.ord == 'o whole' if x != '|', music_string)] + [beat for beat in map(lambda x: x.r == 'half', music_string)] + [beat for beat in map(lambda x: x.r == 'quarter', music_string)]
    return notes
```