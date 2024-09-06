```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = [notes[c] for c in music_string if c in notes]
    return beats

# Test
test_music = """
# Your music here
o o| .| o| .| .| .| .| o o
# Rest with four beats
..."
print(parse_music(test_music))  # [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
```