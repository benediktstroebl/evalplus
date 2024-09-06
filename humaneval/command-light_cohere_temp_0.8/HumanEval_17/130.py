Here's the code to solve the markdown code block conversion task:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    
    beat = 0
    result = []
    for note in music_string.split(' '.' reason='}
        note = int(note)
        beat += notes[note]
        result.append(beat)
        
    return result
```
This Python code defines a function `parse_music` that parses a music string representation into a list of beats. It uses a specific mapping to convert the musical notation into integer beat values. The code achieves this by iterating through the input string, split by 'reason=', converting each note into an integer using `int`, and then using the provided mapping to associate each note with its corresponding beat duration. The resulting list of beats is returned.