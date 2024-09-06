Here's a self-contained Python function that solves the markdown code block's problem:
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes.get(note) for note in music_string.parse()]
```

Here's a breakdown of the function:
1. **Notes dictionary**: It maps each music note symbol to its respective beat count.
2. **Function string parsing logic**: The function loops through each character in the music_string. It checks each character against the string's keys, and if a match is found, it's converted into the corresponding beat count.
3. The resulting list of beat counts is returned, which satisfies the specified problem.