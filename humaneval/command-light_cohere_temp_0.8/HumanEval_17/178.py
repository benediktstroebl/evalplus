```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.wide musical_notes_notes_list()  # Format the string to list of notes
    ```
This script defines a function **`parse_music`** that parses a string of musical notes and returns a list of corresponding integer beats. The function utilizes a legend of musical notes, where each character corresponds to a specific number of beats. The function then formats the string to a list of notes, adhering to the legend.