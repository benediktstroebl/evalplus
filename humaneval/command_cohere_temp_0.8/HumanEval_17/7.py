```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.': 1}
    result: List[int] = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_dict.get(char, 0)
        result.append(current_beat)

    return result
```

This script includes a self-contained function called `parse_music` that takes a string of musical notation as input and returns a list of integers representing the number of beats for each note. It uses a dictionary called `beat_dict` to map note characters to their corresponding beat values. The function iterates through each character in the input string, accumulates the beats based on the dictionary, and stores the accumulated value in a list called `result`. The final `result` list contains the number of beats for each note in the input string.