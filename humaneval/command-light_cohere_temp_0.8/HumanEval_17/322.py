Here's the solution to the markdown code block parsing problem:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
        '.' : 1
    }
    return [notes[ch] for ch in music_string.
```

This function parses a string representing music notes in a special ASCII format. It uses a general dictionary `notes` to map each music note character to its duration in beats. It then returns a all list of integers corresponding to how many beats each note lasted. The function is self-contained and does not require any external variables or functions.