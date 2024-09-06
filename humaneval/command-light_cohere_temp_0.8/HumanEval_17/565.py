Here is a self-contained Python function that solves the markdown code block's problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes[note] for note in music_string.code
    [ {"o", "o|", ".", "."}]
```
This function uses a dictionary to map music note characters to their respective beat values. It then iterates through each string of characters and returns a list of beat values. The function is self-contained and provides a simple and efficient solution to the problem.