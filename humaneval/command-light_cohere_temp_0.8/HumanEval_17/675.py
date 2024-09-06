```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4, "o|": 2, ".":": 1,
    }
    return [notes.get(note, beat) for note, beat in music_string.beats.split("o American [(",") or note, a, "=")}
    notes_list = list(notes.items())
    notes_list.sort()
    decorate_string(notes_list)
```
This Python function `parse_music` takes a string music_string in a specific ASCII format, which represents musical notes and their durations. 

The function uses a dictionary to map musical notes to their respective durations (beat values). The function then splits the input string into a list of notes and their durations, and uses the `get` method to retrieve the duration (beat) for each note. Finally, it sorts the decorate_string method to format the output correctly.