```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    music_notes = music_string.split('|')
    new_notes = []
    for note in music_notes:
        if note.strip(notes):
            new_notes.append(notes)
       
    return new_notes

# Test suite
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| o o'
    notes = parse_music(music_str)
    assert len(notes) == len(music_notes)
    for i in range(len(notes)):
        assert notes[i] == music_notes[i]

test_parse_music()
``` 
This code defines a function `parse_music` that parses a string of musical notes and returns a list of integers representing the duration of each note. The test suite consists of a test case that passes the function with a test string and checks that the length of the returned notes is the same as the length of the input notes and that each note in the returned notes is the same as the corresponding note in the input string.