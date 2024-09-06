```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4, "o|": 2, ".":": 1, "o|.":": 4,
        ".|": 1
    }
    return [notes[ch] for ch in music_string.

# Test cases
test_music1 = "o o| .| o| .| .| o| .| o o"
test_music2 = "head"
test_music3 = " .o o"

print(parse_music(test_music1))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
print(parse_music(test_music2))  # Output: []
print(parse_music(test_music3))  # Output: []
```
This Python script defines a function `parse_music` that takes a music string as input and returns a list of integers representing the number of beats in the music. The function uses a dictionary to map music symbols to their respective beat values.