```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    patterns = {'o' : [4], 'o|' : [2], '.' : [1]}
    
    result = []
    beats = 0
    for note in music_string.split(' '.' opt'):
        note = note.split(' ')
        result.append(beats)
        beats = patterns[note[0]]

    return result

# Test cases
music_str = '''o o| .| o| .| .| .| o o'''
result = parse_music(music_str)
print(result)
```