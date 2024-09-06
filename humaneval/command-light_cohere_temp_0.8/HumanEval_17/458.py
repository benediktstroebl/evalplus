```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beats = [notes.get(note) for note in music_string.beats = sum(beats)
    return beats
```
This Python function, parse_music, is designed to parse a string representing musical notes in a special ASCII format and return a list of integers representing the number of beats in the music.

The function is self-contained, with the music_string parameter acting as the sole input to the function. Additionally, the function returns a dictionary to map the musical note characters to their respective beat values. 

Note: The function utilizes the sum() function to calculate the total number of beats in the music, which corresponds to the legend provided.