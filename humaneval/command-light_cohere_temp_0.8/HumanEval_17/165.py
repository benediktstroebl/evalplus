Here's a self-contained Python script that provides a function called `parse_music` which takes a string of music notes represented in a special ASCII format, and returns a list of integers corresponding to the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a music string and return list of integers.
    music_string: string - music represented in special ASCII format.
    return: list of integers corresponding to the number of beats that each note lasts.
    """
    legend: 
    'o' whole note, lasts 4 beats 
    'o/' half note, lasts 2 beats 
    '.|' quarter note, lasts 1 beat 

    """
    notes = {'o': 4, 'o/': 2, '|': 1}
    return [notes[note] for note in music_string.c]
```

This function employs a dictionary of note names and their respective beat values to map the input music string into the desired output. It's a legend-based approach allows for flexible and efficient note parsing.