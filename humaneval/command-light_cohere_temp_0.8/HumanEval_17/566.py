```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    
    beats = 0
    beats_found = 0
    time_signature = ''
    current_beat = 0
    
    for char in music_string:
        if char == ' ':
            if beats_found > 0:
                beats += notes[time_signature]
                time_signature = ''
            current_beat = 0
        elif char == 'o':
            current_beat += 1
            beats_found += 1
        elif char in notes:
            time_signature += char
        else:
            current_beat = 0
            beats_found = 0
    
    return beats

# Test the function here
test_music = '''o o| .| o| .| .| .| .| o o'''
parse_music(test_music)
print(beats) # Should print [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```