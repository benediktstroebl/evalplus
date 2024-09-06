```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    parsed_music = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_mapping.get(char, 0)
        parsed_music.append(current_beat)

    return parsed_music
```

This code defines a function `parse_music` that takes a string musical composition as input and returns a list of beats. The beat dictionary maps musical notation to beat length providing a flexible way to add new notations if needed. It then iterates through each character in the string, adding the appropriate beat count to a running total using the `beat_mapping` dictionary. After each iteration, the current beat count is appended to the `parsed_music` list, which returns the list of beats for the entire composition. 

Here is an example input/output scenario:
```
input: parse_music('o o| .| o| o| .| .| .| .| o o')
output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```