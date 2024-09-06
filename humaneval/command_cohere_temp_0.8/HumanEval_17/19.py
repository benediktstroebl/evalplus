```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' + re.escape('|') + '|' + re.escape('.') + '|' + ' '.replace('.', r'|'))
    # Using regex to find all whole, half, and quarter notes in the string
    beats = pattern.findall(music_string)
    # Transforming matches to integers
    return [4 if beat == 'o' else 2 if beat == '|' else 1 for beat in beats]
```

The regular expression pattern uses a combination of literal characters and escaped characters via the `re.escape()` function. This allows us to create a pattern that matches the whole, half, and quarter note representations from the input string.

The `findall()` function searches the input string for all matches of the regular expression. The result is a list of matched beats. Each beat match is transformed into its corresponding integer value (4 for whole notes, 2 for half notes, and 1 for quarter notes), via a list comprehension. 

The final result is a list of integers that correspond to the beats of each note in the input string. 

This approach ensures a clean and efficient solution that achieves both flexibility and performance when parsing the given input strings.

The `parse_music` function is self-contained and can be easily imported and used in other Python scripts or applications to parse musical strings and return their beat durations as a list of integers.  It also follows the typing conventions, specifying the input and return types as `music_string: str` and `-> List[int]`, respectively.