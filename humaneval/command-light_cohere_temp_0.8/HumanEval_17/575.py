Here is a Python script that includes the `parse_music` function along with the associated tests:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    
    notes_indices = music_string.split('|')
    
    return [notes[idx] for idx in map(lambda x: x.split('o of notes_indices[0])]

def test_music():
    test_string = 'o o| .| o| .| .| .| o o'
    
    parsed_notes = parse_music(test_string)
    
    assert parsed_notes == [4, 2, 1, 2, 1, 1, 1, 1, 4]
```
This script defines a function `parse_music` that takes a string of music notes represented in a specific ASCII format. The function splits the the notes and returns a list of corresponding beat counts. The function is then tested using the `test_music` function that contains a test string and asserts the output of the `parse_music` function for that input.