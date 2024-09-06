```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    music = ['o', 'o|', '.', 'o', '.', '.', '.', '.', 'o', 'o']
    beats = [notes[i:i+4] for i, e in enumerate(music)] + [notes['o']*4]
    return beats

# Test the function
print(parse_music('o o| .| o| .| .| .| .| o o'))
```