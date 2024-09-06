```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')').
    notes = [int(note.strip()) for note in notes]
    return notes

# Test cases for function
test_music = """
    'o o| .| o| .| .| .| .| o o'
    [4, 2, 1, 2, 2, 1, 1, 1, 4] # Answer: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
"""

test_music_err = """
    O
o| .| o| .| o
"""

if parse_music(test_music_err) != test_music:
    print('Error: Function did not return correct notes')

if parse_music(''.join() != []) or parse_music('o o| o .| .') != [4, 2, 1, 2]:
    print('Error: Function did not handle empty string or single characters correctly')

print("Test passed")
```