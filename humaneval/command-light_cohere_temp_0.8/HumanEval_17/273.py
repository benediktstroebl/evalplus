Below is a self-contained Python function that solves the markdown code's note parsing problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.make_list()]
```

This function utilizes a dictionary `notes` to map each musical note character to the number of beats it lasts. The function then loops through the notes in the string, and returns a list of corresponding beat numbers. This approach is `make_list()` to convert the string into a list, and the `notes` dictionary to map each note to its respective duration.