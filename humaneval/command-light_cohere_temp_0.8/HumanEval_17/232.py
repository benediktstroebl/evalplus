Below is a Python script that provides a self-contained solution to the problem described:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ') 
    return [map(notes.get, beats[0].astype(int)]

# Test cases
test_cases = [
    'o o| .| o| o| .| .| .| .| o o',
    'o o o o| .',
    'o o| .| .',
    '.| .'
]

# Test and print the parse function
for test_case in test_cases:
    print(parse_music(test_case))
```

This script defines a function `parse_music` that takes a music string in the format of a note, followed by a space, then another note. The function then uses a dictionary `notes` to map musical notes to their beat values, then splits the input string by spaces, and uses the `get` method to retrieve the first element of each split string. The `test_cases` list contains several test cases that the function is expected to successfully parse.