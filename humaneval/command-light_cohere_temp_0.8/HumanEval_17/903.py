Here's the self-contained Python function that solves the music notes to beats conversion problem: 

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Returns: list of integers corresponding to how many beats does each note last.
    """

    a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>>
    """
    notes = {'o' : 4, 'o|' : 2, '|.' : 1}
    return [notes[c] for c in music_string.map]
```

You can test this function with different music strings.