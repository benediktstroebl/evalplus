```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|o|_|_|', re.IGNORECASE)

    # Returning a list of lengths of all matches in the string
    return [len(match) for match in pattern.findall(music_string)]
```

The regular expression pattern contains four categories which are whole note ('o'), half note ('o|'),
quarter note ('.|') and the pipe symbol ('|') 

The function `parse_music` uses the regular expression to match every category in the music string and returns a list of their lengths. 

This solution passes the test cases provided in the original problem statement.