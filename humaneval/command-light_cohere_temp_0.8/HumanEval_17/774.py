```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beat_counter = lambda c: notes.get(c[0], 4 if c.isalpha() else 2 else 1)
    
    notes_map = {c: beat_counter(c) for c in music_string}
    
    return [notes_map[c] for c in music_string]

# Test the function with various inputs
test_music = parse_music
test_music('o o| .| o| .| .| .| .| o o')
test_music('o o o o| | o o o| o o o o')
test_music('.|o|')
test_music('o| .')
test_music('o| .o')
```
The parse_music function in this Python script is intended to process a musical notes input and output a list of corresponding beat numbers. The beat_counter function is used to determine the beat duration for each note, and the notes_map maps the musical notes to their corresponding beat numbers. 
The function is then tested with a variety of inputs.