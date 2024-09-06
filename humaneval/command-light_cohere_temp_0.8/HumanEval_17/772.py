Here is a Python script that demonstrates the creation of a self-contained function to solve the given markdown code block's problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.parse(''.
```
This code defines a function named **parse_music** that takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to the number of beats for each note. The function utilizes a dictionary to map the musical notes to their respective beat counts.