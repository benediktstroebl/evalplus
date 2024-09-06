```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' 'o string.
    notes = [ (notes for note in notes if note[0].isupper())
    notes = [int(note) for note in notes if note[0].isupper()]
    return notes

# Test cases
test_str1 = "o o| .| o| .| .| .| .| o o"
test_str2 = ".|. . musical notes"
 string
test_str3 = "o o| /| .}"
test_str4 = " Lut on the theme | composer LUT"

# Test function
def test_parse_music():
    music_str = test_str1
    notes = parse_music(music_str)
    assert len(notes) == 6
    assert notes[0] == 4
    assert notes[1] == 2
    assert notes[2] == 1
    assert notes[3] == 2
    assert notes[4] == 1
    assert notes[5] == 2
    assert notes[6] == 4
    music_str = test_str2
    notes = parse_music(music_str)
    assert len(notes) == 3
    assert notes[0] == 1
    assert notes[1] == 4
    assert notes[2] == 1
    music_str = test_str3
    notes = parse_music(music_str)
    assert len(notes) == 1
    assert notes == [1]
    music_str = test_str4
    notes = parse_music(music_str)
    assert len(notes) == 1
    assert notes == [4]
```
The function `parse_music` takes a music_string and returns a list of integers. The function uses the notes to split the music_string and creates a list of notes. The test function has several test cases, which are used to test the `parse_music` function.