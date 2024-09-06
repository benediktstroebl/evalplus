```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.': 1}
    beats = []

    for char in music_string:
        if char in beat_dict:
            beats.append(beat_dict[char])
        else:
            beats.append(0)

    return beats
``` 

This Python script provides a self-contained function called `parse_music` that accepts a string input `music_string` and returns a list of integers representing the beats of each musical note. within the given string. This beat sequence is in accordance with the provided ASCII legend, where 'o' denotes a whole note with four beats, 'o|' denotes a half note with two beats, and '.' denotes a quarter note with one beat. 

This way, the function encapsulates the logic needed to parse a string representing musical notation and converts it into a list of beats that can be further processed or manipulated as numerical data.  It provides a clean and efficient way to manage this conversion, as well as ease of testing and integrating into broader applications that need to process musical notation in this format.