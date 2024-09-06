```python
from typing import List

 Patterns = {
    'o': 4,
    'o|': 2,
    '.|': 1,
}

def parse_music(music_string: str) -> List[int]:
    result: List[int] = []
    beat = 0

    for char in music_string:
        beat_length = Patterns.get(char)
        if beat_length: 
            beat += beat_length
            result.append(beat)
        else: 
            beat //= 2

    return result
``` 

This approach uses a dictionary `Patterns` to associate beat lengths with each musical notation. It iterates through the input string, checking each character against the dictionary to accumulate the total beat value. Non-note characters are ignored, treating them as dividers that divide the current beat value by 2. The final beat value for each note is added to the result list.

To use this code simply add it to a Python file (e.g., `music_parser.py`), and run the file. This will output the result of the parsing process of the given input.