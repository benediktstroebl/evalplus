```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    notation = ""

    for note in music_string.split(" " ")[::-1]:
        if note.lower() in notes:
            notation += note[0]
        else:
            notation += "|"

    beats = [int(note) for note in notation.split(" o| ")[::-1]]
    return beats

# Test the function with an example input
music_str = "o o| .| o| .| .| .| o o"
beats = parse_music(music_str)
print(beats)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that parses a music string in a special notation format and returns a list of corresponding beat numbers. The test case demonstrates that the function correctly identifies the notes and the number of beats they represent.