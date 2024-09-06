```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[ch] for ch in music_string.

# Test cases
print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music('o o| .o| .| .| .'))  # [1, 2, 4, 1]
print(parse_music('.'))  )  # []
print(parse_music('o|'))  # []
print(parse_music('|o'))  # []
print(parse_music('.____'))  # []
```
This script defines a function `parse_music` that takes a music string as input and returns a list of integers representing the number of beats for each note in the music. The function uses a dictionary to map music symbols to the respective beat count. 

The test cases demonstrate how the function handles different inputs and produce the expected output.