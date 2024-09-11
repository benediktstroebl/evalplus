### Music Note Parser
#### Parse Musical Notes String into List of Beats

Below is a Python script that defines a function `parse_music` to parse a string representing musical notes in a special ASCII format.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Returns a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    notes_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Use a list comprehension to replace each note with its corresponding beats
    beats = [notes_beats[note] for note in notes]

    return beats

# Example usage:
music_string = 'o o|.| o| o|.|..|..|..o o'
print(parse_music(music_string))
```

In this script, we define a dictionary `notes_beats` to map each note to its corresponding beats. We then split the input string into a list of notes, and use a list comprehension to replace each note with its corresponding beats. Finally, we return the list of beats.