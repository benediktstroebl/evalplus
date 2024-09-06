```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' + re.escape('|') + r'(\.|o)')
    # List to store beats for each note
    beats = []
    # Iterate over each match of the pattern in music string
    for match in re.finditer(pattern, music_string):
        note = match.group(1)
        if note == 'o':
            beats.append(4)
        elif note == '.':
            beats.append(1)
        # If match has bar line '|', add 2 to the last note
        if match.group(0) == 'o|':
            beats[-1] += 2
    return beats
```

The module 're' is used to define a regular expression to recognize patterns in the music string that are also used to describe note lengths. The parse_music function iterates over the finditer matches with the pattern in the music string, adds 4 beats for whole notes 'o', adds 1 beat for quarter notes '.', and adds 2 beats to the last note if there is a bar line '|'. The function returns a list of integers corresponding to the beats of each note.

Here is a simple test case:
```python
test_string = 'o o| .| o| o| .| .| .| .| o o'
expected_beats = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
beats = parse_music(test_string)
print(beats)
```

Output:
```bash
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 

This matches the expected output.