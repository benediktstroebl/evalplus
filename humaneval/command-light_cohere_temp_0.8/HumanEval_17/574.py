```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.test_music('o
            o o| .| o| .| .| .| .| o o')]
``` 
This function parses a music string representing musical notes in a special ASCII format. It uses a provided dictionary of notes, each key of which corresponds to a certain number of beats. The function works by converting each "note" in the music string to its corresponding beat value, and then constructs a list of these values.