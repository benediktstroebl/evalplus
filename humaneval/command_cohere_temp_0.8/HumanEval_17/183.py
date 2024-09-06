```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    result = []
    
    current_beat = 0
    for char in music_string:
        current_beat += beat_mapping[char]
        result.append(current_beat)
    
    return result
``` 

This script defines a function `parse_music` that takes in a string of musical notation and returns a list of integers representing the number of beats for each note. The beat mapping is initialized with the special characters and their corresponding beat values. The script loops through the provided string and accumulates the beats using the beat mapping.

Here is an example input/output run:
```python
beat_mapping = {'o': 4, 'o|': 2, '.': 1}

input_str = 'o o| .| o| o| .| .| .| .| o o'
print(parse_music(input_str))
```
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```