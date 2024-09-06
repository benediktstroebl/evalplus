```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    
    beats = [0] * 4
    for note, beat in notes.music_string.strip():
        fast_music_string = f'{note}|{beats[-1]}{note}')
    beats.append(int(fast_music_string))
    return beats

# Test cases
test_music = '''o o| .| o| .| .| o o'''
test_music_beats = parse_music(test_music)
assert len(test_music_beats) == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
```