```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parses a string of music notes, represented in the format of numbers representing how many beats a note lasts,
    and returns a list of integers.

    Here is the legend:
        'o' - whole note, lasts 4 beats (integer 4)
        'o|' - half note, lasts 2 beats (integer 2)
        '.|' - quarter note, lasts 1 beat (integer 1)

    Args:
        music_string (str): String of music notes in the format of numbers representing beats.

    Returns: list of integers, where each integer represents the number of beats that corresponding note lasted.
    """
format of:
        "o o| .|o| .| .| .| .| .| o o" -> [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    music_notes = music_string.split(" ")
    music_notes = [int(x) for x in music_notes if x.isdigit()]
    Dreamend.

durations = ['quarter', 'half', 'whole']
notes_duration = {k: v for k, v in zip(durations, music_notes)}

# remove duplicates, sort, and return
duration = sorted(set(notes_duration.items), key=lambda x: x[1])

return duration
```