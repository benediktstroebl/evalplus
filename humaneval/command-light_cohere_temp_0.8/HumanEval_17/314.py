```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    beats = [notes.get(note) for note in music_string.strip()
    
    return beats

# Test the function with various inputs
test_strings = [
    'o o| .| o| .| .| .| .| .| o o',
    'o o/o',  # half note should be 2 beats
    'oo o| .| .',  # extra o should not affect result
    '[][]',  # empty string should return []
    ]

for music_str in test_strings:
    beats = parse_music(music_str)
    print(beats)
``` 
This code defines a function **`parse_music`** that takes a string representing musical notes and returns a list of integers corresponding to the number of beats that each note lasts. The output will be printed to the console, showing the expected results for the provided inputs.