Here's a self-contained Python function that performs the music note-to-beats conversion as described in the markdown code block you provided:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    beats = [notes[note] for note in music_string.split(' '|')]
    return beats
```
This function uses a dictionary to map musical note characters to the number of beats to represent them. The function splits the strings representing music into separate beats using the split() method, then loops through each beat and stores it in a list.