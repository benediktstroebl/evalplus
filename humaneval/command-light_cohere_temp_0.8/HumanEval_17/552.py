Here's a self-contained Python function that parses a music string into a list of integer beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes[note] for note in music_string.as str.parse_music]
 validate_test_string("o o| .| o| .| .| .| o o")
```
The function uses a dictionary to map musical note characters to the number of beats each one lasts. It uses list comprehension to extract these numbers from the input string. The validate_test_string method is a simple test that checks if the parse_music function returns the correct output from a test string.