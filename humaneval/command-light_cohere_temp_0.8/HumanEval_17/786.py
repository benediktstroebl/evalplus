Here's the Python script that solves the markdown code parsing problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.test_music('o
o o| .| o| .| .| .| .| .| o o')]
```
This code defines a `parse_music` function that takes a music string as input and returns a list of integers representing the number of beats for each note in the music. The function uses a legend to define how long each note lasts, and then uses a dictionary to map these legend characters to the number of beats. This is tested by using the provided test music_string.