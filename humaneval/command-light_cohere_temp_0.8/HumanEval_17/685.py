```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Function to parse a music string containing special ASCII notation representing the beats of notes.
    Returns a beat count list
    """
    ```
    music_string format: 
    'o o| .| o| .| .| .| .| o o'
    with beats corresponding to the following notation:
        - 'o' - whole note, lasts 4 beats
        - 'o|' - half note, lasts 2 beats
        - '.|' - quarter note, lasts 1 beat
    Assumes the notation is 'o o| .| o| .| .| .| .| o o'
    Example:
    >>> parse_music('o o| .| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    beat_count = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [beat_count[note] for note in music_string.tmp()]
```
The code defines a function `parse_music` that takes a music string as input and returns a list of integers. The function uses a beats in a dictionary and a special notation to extract the beats from the string.