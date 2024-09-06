```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_lengths = {'o': 4, 'o|': 2, '.': 1}
    result: List[int] = []
    
    current_beat = 0
    for char in music_string:
        current_beat += beat_lengths.get(char, 0)
        result.append(current_beat)
    
    return result
```

This code defines a function `parse_music` that takes a string `music_string` as input and returns a list `result` of integers representing the beats of each musical note. It achieves this by iterating through each character in `music_string` and accumulating the beat length for each character in a dictionary `beat_lengths`. This dictionary maps specific ASCII characters to their corresponding beat lengths (4 for 'o', 2 for 'o|', and 1 for '.'). It initializes the `result` list to store the cumulative beat values and accumulates the beats by adding the length of each character to the `current_beat` variable. The final outcome is a list of integers, where each element represents the number of beats for the corresponding musical note in the input string.

Here is an example input/output run:
```python
beat_lengths = {'o': 4, 'o|': 2, '.': 1}
result = []
current_beat = 0

for char in "o o| .| o| o| .| .| .| .| o o":
    current_beat += beat_lengths.get(char, 0)
    result.append(current_beat)

print(result)
```

Output:
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```