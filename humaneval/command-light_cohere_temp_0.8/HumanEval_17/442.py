```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o|.' : 2}
    beats = [notes[i] for i in music_string.split(' '|')]
    string_beats = "".join(beats)
    beats = [notes[char] for char in string_beats if char in notes]
    return beats

# Test case
music_str = 'oo o| o .| o| .| .| .| o o'
beat_list = parse_music(music_str)
print(beat_list)  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 
This script defines a function called **parse_music** that takes a string of music notes as input and returns a list of integers that represent the number of beats that each note lasts.  The script then provides a test case to the function to ensure it is working correctly.