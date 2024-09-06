```python
from typing import List

pattern = 'o|^.<|o|o>'


def parse_music(music_string: str) -> List[int]:
    result = []
    curr_note = 4
    for char in music_string:
        if char == 'o':
            result.append(curr_note)
        elif char == '|':
            curr_note //= 2
        elif char == '.':
            curr_note //= 4
        else:
            raise ValueError(f"Unexpected character {char} found!")
    return result
```

The algorithm for the function is as follows:
1. Initialize the `result` list and `curr_note` to 4 (whole note).
2. Iterate over characters in `music_string`.
3. If the character is `'o'` push the current note to the result.
4. If the character is `'|'` divide the current note by 2.
5. If the character is `'.'` divide the current note by 4.
6. If the character is none of the above, raise a `ValueError`. 

The code also has a constant `pattern` that is used in the docstring and test, this constant defines the format example to be used when documenting and testing the function. 

This script will parse a music string and return a list of integers corresponding to the number of beats each note lasts.