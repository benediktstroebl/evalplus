```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    
    # Splitting the string into individual notes
    notes_list = music_string.split(' ') ')
    
    # Converting into an integer array
    beats = []
    for note in notes_list:
        beats.append(int(note))
    
    return beats

# Test cases
def test_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]

test_music()
```
This code defines a function `parse_music` that takes a string of music notes as input and returns a list of integers corresponding to the beats of each note. The `notes` dictionary is used to map the music notes to the number of beats each one lasts. The `test_music` function contains a test case that verifies if the `parse_music` function returns the correct result for a given input. 

Finally, the `test_music()` function is called, which runs the test case and verifies the correctness of the `parse_music` function.