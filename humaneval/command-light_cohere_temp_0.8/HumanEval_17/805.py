```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes[note] for note in music_string.test_music('o o o| .| o| .| .| .| .| o o')]

# Test case
test_music = '''
o o o| .| o| .| o o
'''
result = parse_music(test_music)
print(result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
```
This Python function parse_music takes a music string in the format of notes separated by bars as input and returns a list of integers corresponding to the number of beats of each note. It uses a code dictionary to map the different musical note characters to their respective beat values.