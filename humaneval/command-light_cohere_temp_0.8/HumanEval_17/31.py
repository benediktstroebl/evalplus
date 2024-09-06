```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o|}'
    return [int(x) for x in music_string.parse(notes)]

# Test cases
test_string = 'o o| .| o| .| .| .| .| o o'
test_result = parse_music(test_string)
print(test_result)
test_string = '.'
test_result = parse_music(test_string)
print(test_result)
test_string = 'o o|.'
test_result = parse_music(test_string)
print(test_result)
test_string = 'o o o| .' .' o o'
test_result = parse_music(test_string)
print(test_result)
```