Here is a Python script that defines a function, `parse_music`, which takes a string of music notes and returns a list of integers representing the duration of each note in beats:
```python
from typing import List
import re

def parse_music(music_string: str) -> List[int]:
    notes = re.search("\³(.+)\¨",", music_string)
    durations = [int(x.group()) for x in notes]
    return durations
```
The `re` module in Python provides support for searching and matching regular expressions, which is used in this script to split the music notes. The function then returns a list of durations in beats for each note.