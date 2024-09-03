```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    NOTE_PATTERN = re.compile(r'(?P<whole_note>o)|(?P<half_note>o\|)|(?P<quater_note>.\.|o\|\.')
    
    # Defining a function which takes a string as an input and returns a list of integers.
    beats = []
    for match in NOTE_PATTERN.finditer(music_string):
        note = match.group()
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        else:
            beats.append(1)
    return beats
```

This script utilizes a regular expression to match notes in the input string and determine their corresponding beats. Afterward, it compiles these beats into a list, which is then returned. 

To improve this solution, one could utilize specialized Python libraries, such as `music21`, which are more adept at processing complex musical data. 
However, given the parameters of the provided problem, the current solution offers a straightforward and easily interpretable approach.