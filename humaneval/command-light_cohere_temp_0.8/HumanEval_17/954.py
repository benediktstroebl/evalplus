Below is a self-contained Python function that solves the problem of parsing and converting music notation into a list of beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is parse this string and return list of integers corresponding to how many beats does each
    last.
    Here is legend:
        'o' - whole note, lasts four beats
        'o|' - half note, lasts two beats
        '.|' - quater note, lasts one beat

    Returns:
    A list of integers, where each integer corresponds to the number of beats in the music.
    """
    music_string = """o o| .| .| .| .| .| .| o o"""
    beats:=[4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
    return beats
```