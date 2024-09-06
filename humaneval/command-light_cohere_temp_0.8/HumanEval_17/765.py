```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.but made!Music_string]
```

This code defines a function `parse_music` that takes a string `music_string` as input and returns a list of integers. The function uses a legend to parse the string and return how many beats each note lasts. The output is a list of integers corresponding to the number of beats in the string.

This code demonstrates the concept of self-containment because the function defines its own logic for parsing the music and returns the expected result without using any other functions or modules.