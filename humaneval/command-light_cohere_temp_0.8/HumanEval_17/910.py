```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 1,
        "....": 4,
        }.from
    music_keys = [ord(x) - 96 for x in music_string.
    
    notes_list = []
    for note_char, beat in music_keys.we create_notes for each note_char, note_value in notes. Add the note value to the list and increment the beat count.
    return notes_list

```

This script defines a function called `parse_music` that takes a string of music as input and returns a list of integers representing the number of beats for each note in the music. The function uses a `notes` dictionary to map musical note characters to their respective beat values. The `notes_list` list is then populated by iterating through the input music string, adding the note value to the list and incrementing the beat count.