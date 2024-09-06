```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[char] for char in music_string.
# Test case
 We should be able to run the function and print the expected output
parse_music('o o| .| o| .| .| .| o o')
[4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
```