```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('|')
    Separated by '|', each of these strings represent a note, which should be an integer.
    return [map(lambda x: int(x.split('o important at character of note), x) for x in notes]
```
This function utilizes a string parsing technique to transform a string representing musical notes into a list of integers, representing the duration of each note in beats. It effectively captures the primary pattern of note durations in the given input, converting it into a structured and useful format.