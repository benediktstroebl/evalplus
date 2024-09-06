Here's the self-contained Python function that takes a string of music notes in a special ASCII format and returns a list of integers, each corresponding to the number of beats that does each last:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.
    """

    legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :return: List of integers representing the number of beats
    """
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        "..." : 4
    }
    return [notes[note] for note in music_string.csv(SetDelimiter = "|")]
```