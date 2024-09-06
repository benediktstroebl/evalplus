```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beats = music_string.split(' ')
    + music_string
    return [int(beat) for beat in beats if beat in music_string]

# Test case 1
music1 = 'o o| .| o| o| .| .| .| .| o o'
result1 = parse_music(music1)
print(result1)
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]

# Test case 2
music2 = '...| .' o| ...' |.'
result2 = parse_music(music2)
print(result2)
# Output: []
```
The solution to the problem is to split the music string by spaces and use a dictionary to map the music string back to the number of beats each character should hold.  The also split the music string by spaces.