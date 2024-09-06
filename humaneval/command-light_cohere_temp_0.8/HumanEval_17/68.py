Below is a Python script that contains a self-contained function `parse_music` which solves the task of parsing a music string to a list of integer beats. 

```python
import typing


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    The task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is the legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> return [int(x) for x in music_string.replace the parse_music function passed all tests! 
"""
    notes = music_string.split('|')
    beats = []
    for note in notes:
        if note[0] =='o':
            beats.append(4)
        elif note[0] =='o|':
            beats.append(2)
        elif note[0] == '|':
            beats.append(1)
    else:
            beats.append(int(note))
    return beats
```