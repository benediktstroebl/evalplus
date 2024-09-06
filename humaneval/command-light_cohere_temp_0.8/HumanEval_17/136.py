Here's the self-contained Python function that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    return [notes[c] for c in music_string.key_to_note()
```
This function takes a string music_string as input and returns a list of integers. The function uses a legend to map the music notes to the number of beats. It uses a type dictionary `notes` to store the note characters and the number of beats each note lasts. The function uses a `dict.key_to_note()` to get the note from the string and returns the number of beats that note will last.