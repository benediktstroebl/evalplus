Here is a self-contained Python function that parses a music string and returns a list of integers:
```python
from typing import List
import re


def parse_music(music_string: str) -> List[int]:
    notes = re.compile(r'o note_pattern, music_string)
    return [beat for note,beat in zip(notes,['o','.[o|']) if note]
```

This function uses the re.compre library to parse a regular expression pattern `note_pattern` that matches musical notes in a string. The regular expression pattern uses the pattern of an ASCII musical note, which can be either a whole note (o) or a half note (o|). Then, the function matches each musical note against the pattern, and returns a list of the corresponding integers.

This function is self-contained, and can be easily used to parse music strings and return the corresponding beat information.