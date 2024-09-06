```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    nbeats = len(music_string)
    
    beats = [notes.get(char, beats) for char in music_string if char in notes]
    
    return beats
def test_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    beats = parse_music(music_str)
    
    print(beats)
```