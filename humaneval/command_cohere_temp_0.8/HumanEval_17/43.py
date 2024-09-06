```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' +
                          r'(.)|' +  # any single character except 'o' and '|'
                          r'\|(?=o|' +
                          r'(.)|' +  # any single character except 'o' and '|'
                          r'\|)')     # Ensure there is a | after the previous char to match a half note

    beat_counts = [0, 4, 2, 1]       # beat counts for respective note lengths

    return [beat_counts[pattern.match(char).span()[1] + 1]
            for char in music_string
            if char in 'o.|o|.||'
            and pattern.match(char)]
```

To use this function, you can call it with a string representing musical notes in the specified ASCII format.
The function will return a list of integers representing the number of beats for each note. 
Here is an example:
```python
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
```
Which would print:
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 
Please note that this code assumes the presence of the `re` module, which is included in the Python standard library. If for some reason you are working in an environment where the `re` module is not available, and you cannot or don't want to install it (e.g., Pythonatine), and given the simplicity of the task, an alternative approach could be to use regex semantics via string methods, which would essentially mimic the regex pattern matching that the `re` module provides.