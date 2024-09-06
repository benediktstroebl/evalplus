```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
    }
    return [notes.get(note) for note in music_string.into()
```
The above code defines a function `parse_music` that takes a string representing musical notes in a special ASCII format, and returns a list of integers corresponding to the number of beats in each music.

The code uses a dictionary `notes` to map musical notes to the duration of each note in beats. The code uses the to iterate over the notes in the string and return the corresponding number of beats. 

Would you like to break down the logic of the code?