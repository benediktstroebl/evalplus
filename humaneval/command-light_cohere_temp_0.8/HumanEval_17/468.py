Here's the solution:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = [notes[k] for k in music_string.split(' '|')]
    
    return beats
```
This Python code defines a function `parse_music` that takes a music_string as input and returns a list of integers representing the number of beats in the music. It uses a predefined dictionary `notes` with keys representing musical notes and their corresponding beat values. 

This function splits the music_string by vertical bar `|`, extracts the beat values corresponding to each note, and stores them in a list. This effectively solves the final task of parsing a music note representation into its corresponding beat values.