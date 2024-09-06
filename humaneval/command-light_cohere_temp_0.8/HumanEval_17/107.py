```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('o integrity_ pattern, we can split this string using string. The split function, and store the result in a list. For simplicity, we use a regex pattern to split the string by spaces.

for i, note in notes:
    if note == 'o':
        yield 4
    elif note == 'o|':
        yield 2
    elif note == '.|':
        yield 1
    else:
        raise ValueError("Invalid note. Note must be either 'o', 'o|', '|', or '.'")

Here is the solution that passes all tests: