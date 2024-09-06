Here's the code:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|' : 2,
        '.' : 1,
    }
    return [notes[ch] for ch in music_string.info()["notes"]
```

This code defines a function called **`parse_music`** that takes a string music_string as input and returns a list of integers corresponding to the number of beats in each note. The function uses a string patterns to match the notes and a dictionary to map the patterns to the number of beats.