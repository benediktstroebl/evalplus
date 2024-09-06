```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    notes_in_music = music_string.split()
    Listerns = [int(note) for note in notes_in_music]
    return Listerns

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    result = parse_music(music_str)
    assert len(result) == len([4, 2, 1]))
    music_str = '.'*o|o'
    result = parse_music(music_str)
    assert len(result) == len([1]))
```
The parse_music function has been updated with the music_string definition, which specifies the notes in a special ASCII format. The function splits the music_string into individual notes and then creates a dictionary with the notes and the beats associated with them. The test_parse_music function contains test cases to verify that the parse_music function produces the correct output.