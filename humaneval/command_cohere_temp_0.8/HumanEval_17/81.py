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

This script defines a function `parse_music` that takes in a string representing musical notes in the specified ASCII format. It maps the characters to their corresponding beat values and stores them in a dictionary. It then iterates through each character in the input string, adding the appropriate beat value to the `current_beat`, and appends the resulting value to the `result` list. Finally, it returns the list of beats. 

This solution works without importing any additional modules, but assumes the downstream context has the `beat_mapping` dictionary defined appropriately. 

This approach assumes that the input string will contain only the valid punctuation characters 'o', 'o|', and '.'. Any other characters in the input will be ignored.