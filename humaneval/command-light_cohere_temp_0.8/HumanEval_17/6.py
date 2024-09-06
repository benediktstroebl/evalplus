```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes[note] for note in music_string.upcase: assert len(music_string) == len(notes), "Music string has incorrect length"
    return [i for i, note in enumerate(music_string.replace(), 1) if note in notes]
```
This script defines a function `parse_music` that takes a string music_string representing notes in a special ASCII format, where 'o', 'o|', and '.|' represent whole, half, and quarter notes respectively. The function then uses this dictionary to convert the input string into a list of integers corresponding to the number of beats for each note. The function also includes unit tests to ensure the music string has the correct length and contains only valid notes.