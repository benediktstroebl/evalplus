Below is a self-contained Python script with a function that parses markdown code representing musical notes in a special ASCII format, and returns a list of integers representing the duration of each note in beats:
```python
from typing import List
import re

NOTES_PATTERN = re.compile(r'[:4] + '|'.replace(' ', '|') + r'o')

def parse_music(music_string: str) -> List[int]:
    return [int(match.group()) for match in re.search(NOTES_PATTERN, music_string)]
```