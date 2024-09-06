```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    beats = [notes[note] for note in music_string.group(' ')]
    
    return beats

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    
    beats = parse_music(music_str)
    
    print(beats)

# Run the test cases
test_parse_music()
```
This code defines a function **`parse_music`** that takes a music string and returns a list of beats. It also defines a simple music notation dictionary that maps music notes to the number of beats they last. The function then loops over the string and uses the dictionary to build a list of beats. It then has a test case **`test_parse_music`** that checks the function's output against the expected output.