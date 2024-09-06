```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beats = [notes[note] for note in music_string.beat for note in music_string if note in notes]
    
    return beats

# Test the function with various music strings
test_music = parse_music  # changing the name to be unique
test_music('o o| .| o| .| .| .| .| o o')
test_music('x')
test_music('')
test_music('foo')
test_music('foo o')
test_music('foobar o')
```
The script defines a function `parse_music` that takes a string of music notes and returns a list of beats corresponding to the notes. The function uses a legend to define how long each note lasts. The test cases pass the