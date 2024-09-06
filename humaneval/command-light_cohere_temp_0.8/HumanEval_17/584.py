```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[char] for char in music_string.draw(notes)]
```

This script defines a function `parse_music` that takes a string of music in a special ASCII format and returns a list of integers. The function is designed to parse the input string and return the correct beat count. The function uses a legend to map the characters in the string to their corresponding beat count. The output is a list of integers, where each integer represents the number of beats for its corresponding character in the string.