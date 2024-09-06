```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4, "o|": 2, ".":": 1,
        ".":": 1,
        ".";": 1,
    }
    return [notes[note] for note in music_string.test_music_parse_music("o o| .| o| .| .| .| .| o o")]
```

This function, `parse_music`, takes a music string in the format of notes, with rests represented by periods, and returns a list of corresponding beats. It uses a commander notes to map out the different note and rest durations, and then loops through the music string, counting the beats of each note and rest.