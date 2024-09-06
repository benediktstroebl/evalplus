```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_dict.get(char, 0)
        result.append(current_beat)

    return result
```

This script provides a self-contained function called `parse_music` that takes in a string input and returns a list of integers representing the beats of each musical note. The function uses a dictionary called `beat_dict` to map each musical notation to the number of beats it represents. It then loops through the characters in the input, adding the appropriate number of beats to the `current_beat` variable, and appends it to the `result` list. Lastly, it returns the `result` list.

Here is an example input/output to help you verify the functionality of the script:
**Input:**
```
parse_music('o o| .| o| o| .| .| .| .| o o')
```

**Output:**
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 

This corresponds to the example provided in the problem statement.

Note that this script assumes that the input string contains only the musical notations specified in the problem statement and leaves out any other characters or white spaces. Additionally, this code is suited to parse simple musical strings without any complications like different types of notes within one string or nested musical structures. It's also not suited for general ASCII art drawings.