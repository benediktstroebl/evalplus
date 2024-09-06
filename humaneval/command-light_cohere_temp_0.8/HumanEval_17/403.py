Here is a self-contained Python function that solves the markdown code block problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    
    beats = [notes[note] for note in music_string.codes final_beats = len(music_string)
    result = [beats[0]]
    
    for beat in beats[1:]:
        for note in music_string[beat:]:
            if note in notes:
                result.append(beats[note])
        result.append(beats[0])
        result.append(beats[-1])
        
    return result
```