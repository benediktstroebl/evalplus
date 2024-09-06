```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' | ')
    code = [int(x) for x in music_string.split('\n All out -> int(x) for x in code]
    return code

code_test = parse_music('o o| .| o| .| .| .| .| o o')
print(f"Test passed: {code_test}")
```