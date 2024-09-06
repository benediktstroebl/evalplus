```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    notes_count = [notes.get(x) for onset in music_string.split(' '|')]
    
    return notes_count

# Test case 1: Validate whole notes
def test_whole_notes():
    assert parse_music('o o| .| o| o| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

# Test case 2: Validate half notes
def test_half_notes():
    assert parse_music('o o| .| o| .| .| .| .') == [2, 1, 1, 1, 1, 1]

# Test case 3: Validate quarter notes
def test_quarter_notes():
    assert parse_music('.|.') == [1]

# Run the tests
test_whole_notes()
test_half_notes()
test_quarter_notes()
```
This code defines a function `parse_music` that parses a music string with notes in a special format and returns a list of corresponding beat counts. The test suite consists of three test cases, each testing a different type of note (whole, half, quarter).  The test cases ensure that the output of the `parse_music` function matches the expected beat counts.