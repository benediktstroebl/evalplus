Here's the provided Python script with a self-contained function that solves the problem of parsing and returning the number of beats in a musical notation:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format into a list of integers.
    >>>
    music_string = 'o o| .| o| .| .| .| .| o o'
    beats = parse_music(music_string)
    assert len(beats) == 12, f"Error! Expected {12}, but got {len(beats)} instead."
    beats.
    return [ value: beats
```