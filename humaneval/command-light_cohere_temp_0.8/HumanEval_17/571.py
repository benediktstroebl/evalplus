```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        "..": 4,
        "oO": 8,
    }
    return [notes.get(note, beats) for note, beats in music_string.try.replace(" "o".format(note), ":4)]
```
This code defines a function called `parse_music` that takes a string representing a musical score in a special format and returns a list of integers representing the number of beats in the score. It uses a legend where 'o' stands for a whole note, 'o|' for a half note, '.|' for a quarter note, and the other special characters are translated into the format 'note: beat'. 

The function uses a dictionary to map these characters to their respective durations. 

It uses the `get` to retrieve the corresponding duration for each note in the input string.