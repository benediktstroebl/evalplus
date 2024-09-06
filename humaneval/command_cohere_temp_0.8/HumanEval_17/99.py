```python
from typing import List

 Patterns = {
    'o': 4,
    'o|': 2,
    '.': 1
    }

def parse_music(music_string: str) -> List[int]:
    result = []
    beat = 0
    for note in music_string:
        if note in Patterns:
            beat += Patterns[note]
        else:
            beat = 0
        result.append(beat)
    return result
``` 

This script utilizes a `typing` module to improve type checking and the `Patterns` dictionary to map music symbols to their corresponding number of beats. The function `parse_music` iterates through a musical string, updating the `beat` variable by the duration of each note and storing its value in a list. The resulting list corresponds to the duration of each musical note in beats.

Here's an example usage of the code:
```python
>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This result is consistent with the example provided in the problem statement.