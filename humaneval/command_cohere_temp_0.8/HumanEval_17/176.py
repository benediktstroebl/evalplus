```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    result = []
    
    current_beat = 0
    for char in music_string:
        current_beat += beat_mapping.get(char, 0)
        result.append(current_beat)
    
    return result
``` 

This code defines a function `parse_music` that takes a string input and returns a list of beat durations, as described in the problem statement. It utilizes a beat mapping dictionary to map each character to its corresponding beat duration. It iterates through the input string, accumulating the beat duration by checking the character against the `beat_mapping` dictionary and adding the appropriate duration. Finally, it returns the list of beat durations.