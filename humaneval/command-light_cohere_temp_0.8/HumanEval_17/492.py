```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    
    beats = []
    current_beat = 0
    
    for note in music_string.split(' '.' song '.'
    if note in notes:
        beats.append(current_beat)
        current_beat += notes[note])
    return beats

# Test cases for function
test_music = []
test_music.py test_music('o o| .| o| .| .| .| .| .| o o')
test_music.print(parse_music(test_music))
``` 
This script defines a function `parse_music` that takes a string of music notes and returns a list of beats. The function uses a type hint `List[int]` and the function `notes` to map musical note characters to the beat lengths. 

The test cases use the function `test_music` to create a string of music notes, and then pass it to the `parse_music` function.  The test cases also print the results of the function call to the console.