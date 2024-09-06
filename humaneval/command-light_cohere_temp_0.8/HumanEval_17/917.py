Here is a Python script with a self-contained function that solves the problem of converting a string of musical notes into a list of their durations:
```python
from typing import List
import re

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes in the special ASCII format as input.
    The task is to parse this string and return a list of integers corresponding to how many beats does each note last.
    Here's legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Returns:
    A list of integers, the number of beats each note lasts.
    """
    string match pattern:
        '((o[+-])(o[+-]|.|')*(\'o'|$\n|))'
    """
    pattern = re.compile(r'(('o'[0-]|')*(\'o'|$\n|)'))
    matches = re.findall(pattern, music_string)
    return [int(match[0]) for match in matches]
```
The `parse_music` function uses the `re.findall` function to find all matches of the pattern, and the `int` function is used to convert the match into an integer. This function can be used to parse any string of musical notes in the specified format.