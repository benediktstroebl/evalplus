```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' +
                          r'(\.|o|o|)' +
                          r'|\.|' +
                          r'o|' +
                          r'o|' +
                          r'(\.|o|o|)' +
                          r'|\.|' +
                          r'o|' +
                          r'o|' +
                          r'(\.|o|o|)')

    # Using list comprehension to extract matches and convert them to int
    return [len(list(group)) * 4 // 2 for match in pattern.findall(music_string) for group in match]
```

The code uses a regular expression to match the special ASCII notation and a list comprehension to transform
each match into the number of beats. The `re.compile()` function creates a regex object. The `findall()` function 
lists all substrings where the regular expression matches and the list comprehension calculates new values based on these matches.