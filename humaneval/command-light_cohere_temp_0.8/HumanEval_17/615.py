Here's the self-contained Python function that parses markdown musical notation and returns a list of integers:
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, '|' : 1}
    return [notes[char] for char in music_string.  
```
This code uses a dictionary, `notes` which maps musical note characters to the number of beats that character represents. It iterates through notes by converting the characters in the input string to integers using the dictionary.