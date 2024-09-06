```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    result = [notes[note] for note in music_string.
    
    # Check if the separator is '|'
    if music_string.find('|'):
        string = music_string.split('|')
        separator_idx = music_string.find('|')
    string = music_string[:separator_idx] + '|' + music_string[separator_idx+1:]
    return [int(note) for note in string.
    
# test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    result = parse_music(music_str)
    assert [4, 2, 1] == result
    music_str = 'o o| o'
    result = parse_music(music_str)
    assert [4] == result
    music_str = 'o|.'
    result = parse_music(music_str)
    assert [1] == result
```