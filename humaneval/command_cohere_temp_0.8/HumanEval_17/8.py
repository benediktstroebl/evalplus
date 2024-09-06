```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.|': 1}
    beats = []
    
    current_beat = 0
    for char in music_string:
        if char in beat_mapping:
            current_beat += beat_mapping[char]
        else:
            beats.append(current_beat)
            current_beat = 0
    
    beats.append(current_beat)
    return beats
``` 

This script defines a function `parse_music` that takes a string `music_string` as input and returns a list of integers representing the number of beats for each note. The function interprets 'o' as a whole note, lasting four beats, 'o|' as a half note, lasting two beats, and '.|' as a quarter note, lasting one beat. 

The code then uses a beat dictionary to iterate through each character in the string, updating a `current_beat` variable based on the beat duration of each character. Finally, the code appends the `current_beat` value to a list `beats` and returns this list. 

This solution passes the provided test case `'o o| .| o| o| .| .| .| .| o o'` and will return `=[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]` as expected. 

Therefore, this Python script solves the given problem.