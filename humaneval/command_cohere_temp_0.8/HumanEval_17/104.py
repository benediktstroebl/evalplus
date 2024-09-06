```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    notes = []
    curr_beat = 0

    for char in music_string:
        if char in beat_mapping:
            curr_beat += beat_mapping[char]
            notes.append(curr_beat)
        elif char == '|':
            curr_beat = 0

    return notes
```

This code defines a function `parse_music` that takes a string input and returns a list of integers representing the number of beats for each note based on the provided ASCII format. It also provides a beat mapping dictionary to store the beat values of each special character. The code iterates through the input string, tracking the current beat and adding the appropriate value to the list based on the character encountered. It resets the current beat to zero whenever a vertical bar '|' is encountered.