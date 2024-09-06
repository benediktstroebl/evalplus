```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    pattern = r'(\d+)'
    matches = re.findall(pattern, music_string)
    return [int(note) for note in matches and notes.

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| o o' o'
    expected = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(music_str)
    assert actual == expected
    print('Test passed!

test_parse_music()
```
This Python script defines a function `parse_music` that parses a music string in a specific format into a list of integers representing the beats of notes. The function utilizes a regular expression to identify and extract the note values from the music string, and then maps them back to their correct note symbols. The test case section ensures that the function produces the correct output for the given input music string.