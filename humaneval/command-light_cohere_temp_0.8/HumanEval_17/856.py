Here is a Python script that defines a self-contained function `parse_music` to solve the problem of parsing music notes represented as ASCII format into a list of integers representing the duration of each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    return [notes[char] for char in music_string.
```
This function uses a dictionary `notes` to map music note characters to the number of beats that note lasts.  The function then iterates through each character in the `music_string` and returns a list of corresponding beat counts.