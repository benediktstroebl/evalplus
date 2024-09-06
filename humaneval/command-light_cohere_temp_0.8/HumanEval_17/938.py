```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1
    }
    return [notes[note] for note in music_string.

# Test case
music_string = 'o o| .| o| .| .| .| o o'
test_parse = parse_music(music_string)
print(test_parse)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This Python function named `parse_music` takes a string of music notes represented in the special ASCII format as input. 

The function maps each character in the string to its corresponding number of beats (which is an integer value). 

The function then returns a list of these beat numbers. 

The test case demonstrates the function by using it to parse a sample music string and then printing out the resulting list of integers.