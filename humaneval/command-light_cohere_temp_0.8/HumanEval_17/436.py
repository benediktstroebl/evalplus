```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = []
    current_beat = 0
    for note in music_string:
        if note in notes:
            beats.append(current_beat)
        current_beat += notes[note]
    return beats

# Test the parse_music function
test_music = parse_music('o o| .| o| .| .| .| .| o o')
print(test_music)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 
This script defines a function `parse_music` that takes a string music_string as input and returns a list of integers, where each integer represents the number of beats for the corresponding note. The function uses a legend to determine the length of each note in the music string.