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

This code defines a function `parse_music` that takes a string input and returns a list of integers representing the number of beats for each note. It achieves this by using a dictionary `beat_lengths` that maps note characters to their corresponding beat lengths. It iterates over each character in the input string and adds the beat length for each note to the `current_beat`, which keeps track of the total accrued beat length. Finally, it returns this list of beat lengths. 

This solution adheres to the given test case and provides a functional implementation of the specified function.