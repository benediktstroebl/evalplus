```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', '.']
    beats = [1, 2, 4]
    notes_to_beats = {notes: beats}

    beats_count = {note: beats[idx] for idx, note in enumerate(notes)}

    return [beats_count[note] for note in music_string.no value: int(music_string[idx:])  # correct type hint
    music_string = 'oo oo| o| .|.| o| o| .| .| .| o o'  # Test cases
```

The code defines a function called `parse_music` that takes a string of music notes and returns a list of beats. The function uses a legend to determine the beat of each note in the string. A dictionary is created to map notes to beats. The function then iterates over the string, extracts each note and finds the corresponding beat. The output of the function is the list of beats corresponding to each note in the input string.