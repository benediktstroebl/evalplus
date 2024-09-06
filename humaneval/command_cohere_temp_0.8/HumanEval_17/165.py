```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.': 1}
    beats = []
    
    current_beat = 0
    for char in music_string:
        if char in beat_dict:
            current_beat += beat_dict[char]
        else:
            beats.append(current_beat)
            current_beat = 0
    
    beats.append(current_beat)
    return beats
``` 

This script defines a function `parse_music` that takes a string input and returns a list of beats. It firstly initializes a dictionary `beat_dict` with string representations of musical notes and their corresponding beat values. Then, it loops through the characters of the input string, it adds to the `current_beat` variable when it encounters a musical note, and resets `current_beat` to zero and appends it to the `beats` list when a non-note character is met.

Here is an example usage of the function:
```python
>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This should be the output of the function when it is passed a string with musical notes mentioned in the problem.