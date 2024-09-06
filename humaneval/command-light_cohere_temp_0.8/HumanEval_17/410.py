```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
        '\\"o\\"': 4, 'o\\"|': 2, '\\\.|': 1,
        '\\"o\\"\\|': 4, 'o\\"\\||': 2, '\\"\\\.|\\"': 1,
        'o o': [4, 2], 'o| o': [2, 2], '.| o': [1, 2],
        'o .': [4, 2], 'o| .': [1, 2]
    }
    
    beats = [notes[note] for note in music_string.replace[note.split('|')]]
    
    return beats
```

This function 'parse_music' in Python reads in a string of music notes represented in a special format and returns a list of integers corresponding to the number of beats that each note lasts. The function uses a legend to map the music notes to the beat count.