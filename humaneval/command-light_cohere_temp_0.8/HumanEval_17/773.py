Here is a self-contained Python function that solves the problem of parsing Markdown music codes into a list of integer beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    patterns = {
        'o': 4,
        'o|' : 2,
        '.|' : 1,
    }

    return [patterns[note] for note in music_string.
```
This function uses a dictionary to map musical notes to the number of beats each one lasts. The function then returns a list of these beat numbers corresponding to each musical note in the input string.