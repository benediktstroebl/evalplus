```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    result = [notes[c] for c in music_string.
    return result
 test_string = 'o o| .| o| .| .| .| .| o o'
    test_result = parse_music(test_string)
    assert test_result == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    return result
```