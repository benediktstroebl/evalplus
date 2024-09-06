Here's the self-contained Python function that solves the problem of converting music notes to the number of beats each lasts:

```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a music string containing notes and returns the list of their durations (beats).
    Notes are represented as a specific ASCII format. 

    example:
    'o o| .| o| .| .| .| .| o o'
    Returns:
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    def get_duration(note):
        if note == 'o': return 4
        elif note == 'o|': return 2
        elif note == '.|': return 1
        else: return 0
    
    notes = music_string.split(' ')')
    each_note in notes
    durations = [get_duration(note) for note in notes]
    return durations
```