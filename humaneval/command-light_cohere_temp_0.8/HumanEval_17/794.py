Here is a self-contained Python script that defines a function **`parse_music`** that correctly parses Markdown music codes and returns a list of integers: 
```python
from typing import List
import re

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes represented in special ASCII format.
    The task is to parse this string and return a list of integers corresponding to how many beats does each note last.

    Here is the legend:
    - 'o' - whole note, lasts 4 beats
    - 'o|' - half note, lasts 2 beats
    - '.|' - quarter note, lasts 1 beat

    >>>
    """
    # Regex pattern to match whole, half, and quarter notes
    pattern = r'(?<=[oOo|.]>|[oo])'
    notes = re.findall(pattern, music_string)

    # Convert list of strings to integers
    integers = [int(note) for note in notes]

    return integers
```