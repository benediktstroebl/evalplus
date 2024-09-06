```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' | '')[1:]
    notes = [int(note) for note in notes]
    return notes

# Test the function
test_string = '''
o o| o o| .| o| o o
o o
'''
result = parse_music(test_string)
print(result)

test_string = '''
. whole whole note
o o
o o| o
o o
o o
'''
result = parse_music(test_string)
print(result)
```

This script defines a function `parse_music` that takes a string of music notation as input and splits it by `|`, filtering out the character `O` to split into `notes` and then converting `notes` into integers. The function then returns a list of these integers.