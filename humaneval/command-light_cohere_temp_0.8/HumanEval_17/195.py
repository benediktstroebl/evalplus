Below is a self-contained Python script that defines a function `parse_music` that takes a music string and returns a list of integers, each representing the number of beats for a musical note. 

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Here is the legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> [int123456] = ['o', 4, 2, '.', 1]
    >>> parse_music('o o| .| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    >>> parse_music('o o o o o o o o o| .| .')
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    """
    music_notes = ['o', 4, 2, '.', 1]
    beats = [len(note) for note in music_notes]
    return beats
```