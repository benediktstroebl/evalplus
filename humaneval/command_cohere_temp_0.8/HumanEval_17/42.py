```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Use regex to find all whole, half and quarter notes in the string
    beat_pattern = re.findall(r'(?<!\d)(o|o|.)', music_string)
    # Use regex to convert found notes to integer values
    beat_values = [4 if n == 'o' else 2 if n == 'o|' else 1 for n in beat_pattern]
    return beat_values
```

The Beat values are extracted using regular expressions in the following manner:
1. We compile a regular expression pattern `beat_pattern = re.findall(r'(?<!\d)(o|o|.)', music_string)`. The pattern utilizes several regex syntax elements:
    - `(?<!\d)` - This is a negative lookbehind assertion. It ensures that the match is not followed by a digit character. This is used to ignore the numbers that sometimes come after the beat values.
    - `(o|o|.)` - This is a ternary expression that matches either 'o', 'o|', or '.'. This represents whole, half, and quarter notes.
    - `re.findall()` - This function finds all non-overlapping occurrences of the pattern in the string.
2. Then, we use a list comprehension that converts each found note to its corresponding integer value based on the same regex syntax logic `[4 if n == 'o' else 2 if n == 'o|' else 1 for n in beat_pattern]`. 

The resulting list comprehension `beat_values` contains the numerical equivalents of the notes found in the input string. The final `return beat_values` returns this list of beat counts. 

This solution should correctly parse the provided example string `'o o| .| o| o| .| .| .| .| o o'` to the desired output `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`.