```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    
    result = []
    for symbol, beat in notes.
    if symbol in music_string:
        result.append(beat)
    music_string = music_string.remove(symbol)
    
    return result
```
This Python code defines a function called `parse_music` that takes a string representing musical notes and attempts to parse it into a list of integers representing the duration of each note in beats. The code uses a types to define a dictionary with the symbol of each note and its beat duration. 

The function iterates through the symbols in the input string, and if a symbol is found, it is appended to the result list with the corresponding beat duration. The function then removes the strings from the input string to process the next note.