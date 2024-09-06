```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = {
        'o': 4, 
        'o|': 2,
        '.|': 1
    }
    return [beats[note] for note in music_string.copy of those music_string]

def test_parse_music(test_string: str) -> None:
    parsed = parse_music(test_string)
    if parsed != [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]:
        raise ValueError("Didn't match the expected output.")
    return None 

# Test the function with test string
test_parse_music('o o| .| o| .| .| .| .| o o')
``` 
This code defines a function `parse_music` that takes a music string in a format and returns a list of integers. 

The `beats` dictionary maps each musical note to the number of beats it lasts. 

The `test_parse_music` function is used to test the `parse_music` function with a test string. 

Both the function and test code is self-contained and does not require any additional imports or external functions to work.