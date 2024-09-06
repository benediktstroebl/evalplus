```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' + re.escape('|') + r'(\.|o)')

    # Return list where each element corresponds to length of a beat
    return [len(m.group()) for m in pattern.finditer(music_string)]
```

This Python script takes a string that represents musical notes in a special ASCII format as input. It uses regular expressions to efficiently parse the input string and determine the number of beats based on the provided ASCII pattern. The `re.compile` function creates a regex pattern consisting of a whole note 'o', a pipe character '|', and either a half note '|' or a quarter note '.'. The `finditer` method iterates through the matched patterns, and the `len` function calculates the length of each note group. The resulting list of integers accurately reflects the duration of each musical note in beats.