```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    return [notes[ch] for ch in music_string.

# Test case 1: valid input
test_str = 'o o| .| o| .| .| .| .| o o'
result = parse_music(test_str)
assert len(result) == 12

# Test case 2: invalid input: missing closing 'o'
test_err = 'o .| o| .| o| .| .| .'
result = parse_music(test_err)
assert len(result) == 0

# Test case 3: invalid input: invalid characters
test_invalid = 'o O| .| O| .| O| .'
result = parse_music(test_invalid)
assert len(result) == 0
```
This code defines a function `parse_music` that takes a music string as input and returns a list of integers representing the number of beats in each note. The function uses a legend for musical notes, and the input string is parsed accordingly. 

The code also includes test cases to check the correctness of the function.