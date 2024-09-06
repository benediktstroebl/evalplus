Here's the Python code with a self-contained function:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes[ch] for ch in music_string.
```
This code defines a function called `parse_music` which takes a string music_string as input and returns a list of integers. The function uses a string's characters to map to the appropriate number of beats. It utilizes a string.