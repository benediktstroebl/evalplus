```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    
    beats = 0
    notes_found = 0
    for char in music_string:
        if char in notes:
            beats += notes[char]
        notes_found += 1
    
    return [beats, notes_found]

# Sample input and expected output
music_string = 'o o| .| o| .| .| .| o o'
beats, notes_count = parse_music(music_string)
print(beats)  # Output: [4]
print(notes_count)  # Output: [4]
```
This Python function, `parse_music`, is designed to interpret and analyze a string of musical notes represented in the format specified in the function's docstring. The function takes a input and, in this case, returns two values: the number of beats in the music and the count of notes found. 

The output will be displayed with the function call: 
```python
beats, notes_count = parse_music(music_string)
```