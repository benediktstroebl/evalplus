```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1
    }
    return [notes[char] for char in music_string.

# Test the function with a few inputs
test_strings = [
    'o o| .| o| o| .| .| .| .| o o',
    'hello world',
    '|.#$',
    'o o o o o',
    '['
]
if parse_music(test_strings[0]) != [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]:
    print("Error in test 1")
if parse_music(test_strings[1]) != []:
    print("Error in test 2")
if parse_music(test_strings[2]) != []:
    print("Error in test 3")
if parse_music(test_strings[3]) != []:
    print("Error in test 4")
if parse_music(test_strings[4]) != []:
    print("Error in test 5")
```