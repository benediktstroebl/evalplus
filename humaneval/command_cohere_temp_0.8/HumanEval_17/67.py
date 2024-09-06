```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_conversion = {'o': 4, 'o|': 2, '.': 1}
    result = []
    
    for char in music_string:
        if char in beat_conversion:
            result.append(beat_conversion[char])
    
    return result
``` 

This script utilizes a dictionary called `beat_conversion` to map each ASCII character to the number of beats it represents. The `parse_music` function goes through each character in the `music_string`, and if it exists in the `beat_conversion` dictionary, it appends the corresponding number of beats to the `result` list.

To ensure the accuracy of this solution, you can test it using examples provided in the problem statement like so:
```python
>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 
Ensure that your script returns the expected output for this example and others provided. Test cases are essential to validate the correctness of your solution.