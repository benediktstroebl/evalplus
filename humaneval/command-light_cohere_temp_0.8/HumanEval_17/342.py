Here's a self-contained Python function that takes a string of music notes represented in the special ASCII format, then parses this string into a list of integers representing the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.split(' '|')]
```

This function utilizes a dictionary to map the musical note characters to their respective beat values. The function then splits the string by '|' character, and loops through each resulting string and maps it to the corresponding note in the dictionary. This ensures that only unique note characters are used, and that they are correctly mapped to their respective beat values.