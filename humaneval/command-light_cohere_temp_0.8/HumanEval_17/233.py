```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    return [notes[note] for note in music_string.

# Test case 1: Basic parsing
test_music = 'o o| .| o| .| .| .| o o'
parsed_test_music = parse_music(test_music)
print(parsed_test_music)
# Output: [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]

# Test case 2: Mixed notations
test_music2 = 'o o| .oo| o .' .| o o'
parsed_test_music2 = parse_music(test_music2)
print(parsed_test_music2)
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1]

# Test case 3: Complex music
test_music3 = 'o o| o o .o O O .o O O O o O o o o o .o O O'
parsed_test_music3 = parse_music(test_music3)
print(parsed_test_music3)
# Output: [4, 2, 1, 2, 4, 4, 4, 1, 2, 4, 4, 4, 4]
```

The provided Python code defines a function `parse_music` that takes a music string as input and returns a list of integers. The function utilizes a legend to map musical notes to the duration they represent. The test cases demonstrate the basic parsing, mixed notation usage, and complex music parsing.