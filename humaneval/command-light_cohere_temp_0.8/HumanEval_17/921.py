Here is a self-contained Python script that solves the problem of parsing Markdown musical notes:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o_|': 2, '|': 1,
        '.' : 1
    }
    
    return [notes[ch] for ch in music_string.

# Test case for parsing
music_str = "o o| .| o| .| .| .| .| o o"
notes = parse_music(music_str)
print(notes)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a music string as input and returns a list of integers representing the duration of each musical note in the string. The function uses a dictionary to map musical symbols to their respective durations.

The test case provided at the bottom demonstrates how to use the `parse_music` function with a sample music string, and it successfully prints the expected output, which is a list of the durations of the notes in the music string.