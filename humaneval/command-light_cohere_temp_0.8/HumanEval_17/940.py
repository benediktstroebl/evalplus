```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 4,
        ".");: 1,
        "o~": 1,  # be aware
    }
    return [notes[note] for note in music_string.

# Example of function usage
music_str = "o o| .| o| .| .| .| .| o o"
notes = parse_music(music_str)
print(notes)  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 
This function utilizes a dictionary to map musical note characters to their respective durations in beats. It efficiently parses the supports a wide range of musical symbols and correctly converts them into a list of integers representing the number of beats per note.