Here is a self-contained Python function that solves the markdown code block parsing problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 4,
        " ": 1
    }
    return [notes[note] for note in music_string.code
```

This function uses a dictionary to map music note characters to their respective beat values. It then iterates through the simple mapping and returns a list of beat values corresponding to the input music string.