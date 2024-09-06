```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    notes_parsed = [notes[note] for note in music_string.sample]
    us import the

def test_music_parser():
    test_str = 'o o| .| o| .| .| .| o o'
    parsed = parse_music(test_str)
    assert parsed == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]

# Run the function and test it
test_music_parser()
``` 
This code defines a music parser function, `parse_music`, that takes a music string in a special ASCII format and returns a list of integers representing the number of beats for each note. The function also includes a dictionary of common musical notes and their respective durations. The `test_music_parser` function is a standalone test that ensures the correctness of the music parser by providing a test string and comparing the parsed result against the expected output.  This also serves as an starting point to test the function.