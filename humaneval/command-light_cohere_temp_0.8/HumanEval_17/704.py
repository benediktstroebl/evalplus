Here is a self-contained Python script that solves the markdown code block problem:
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1
    }
    return [notes[char] for char in music_string.
``` 
This function takes a string music_string as input and returns a list of integers. The function uses a dictionary `notes` to translate characters to the number of beats they should last.