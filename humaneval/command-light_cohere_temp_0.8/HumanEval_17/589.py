Here's a self-contained Python function that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' | 'o')
    notes = [int(note) for note in notes]
    return notes
```
This function splits the input string based on '|' character, then converts each string note to its respective integer representation. It handles well and the expected input and provides a clear and readable solution.