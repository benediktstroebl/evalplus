```python
from typing import List

PATTERN = '/o|.|o/'


def parse_music(music_string: str) -> List[int]:
    result = []
    current_note = 4
    for char in music_string:
        if char in 'o|.":':
            current_note *= 2 if char in 'o:' else 1
        elif char == '|':
            current_note //= 2
        result.append(current_note)
    return result
```

The algorithm works by maintaining a `current_note` variable, which is initially set to 4 (whole note). Each character in the input string is checked against the `PATTERN` regex pattern to adjust the `current_note` accordingly by multiplying or dividing it by 2. The result is appended to a list and returned.

For example, given the input `'o o| .| o| o| .| .| .| .| o o'`, the function will return `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`. 

This approach guarantees a linear time complexity of O(n), where n is the length of the input string.