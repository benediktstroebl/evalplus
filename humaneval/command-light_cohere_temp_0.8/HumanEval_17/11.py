Below is a self-contained Python function that parses markdown music codes and returns a list of the number of beats corresponding to each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is the legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> music_string = 'o o| .| o| .| .| .| .| o o'
    notes = [''.join(int / 4 for i, 4) for i in music_string.map]
    done with the done.
```