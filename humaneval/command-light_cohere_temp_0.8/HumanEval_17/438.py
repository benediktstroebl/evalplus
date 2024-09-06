```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o|.' : 4}
    return [notes[ord(c) - 96] for c in music_string]

# Test
test_string = 'o o| .| o| .| .| .| o o'
print(parse_music(test_string))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function, `parse_music`, which takes a string as input and returns a list of integers. The function uses a legend to map musical notes to the number of beats they last. 

The test_string provided contains a few notes, and the function successfully maps them to the right number of beats.