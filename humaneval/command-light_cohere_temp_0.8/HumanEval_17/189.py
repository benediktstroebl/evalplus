```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') '
    [int(note) for note in notes if note.split(' ')[0] == 'o']
    return [beat for beat in notes if beat == '4'] or [beat for beat in notes if beat == '2'] or [beat for beat in notes if beat == '1']

# Test case 1: Valid whole note
test_case1 = 'o o'
result1 = parse_music(test_case1)
assert len(result1) == 4

# Test case 2: Valid half note
test_case2 = 'o o|.'
result2 = parse_music(test_case2)
assert len(result2) == 2

# Test case 3: Valid quarter note
test_case3 = '.|.'
result3 = parse_music(test_case3)
assert len(result3) == 1

# Test case 4: Invalid input
test_case4 = 'asdf df dsft'
with pytest. assert.assert expected_ [ expected exception
 assert parse_music(test_case4) is []
```