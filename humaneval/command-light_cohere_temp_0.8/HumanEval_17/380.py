```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_lst = [notes[char] for char in music_string if char in notes]
    return notes_lst

# Test the function with sample inputs
test_parse_music = parse_music('o o| .| o| .| .| .| .| o o')
test_parse_music.
```
This code defines a function `parse_music` that takes a string of music notes represented in a specific format and returns a list of integers corresponding to the number of beats in each note. 

It uses a dictionary to map the music notes to the respective beat values.  The test the input is a sample string, and the function is tested with this input to ensure it's working correctly.