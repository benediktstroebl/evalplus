```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    music = music_string.split(' '|')
    music_array = []
    for i in range(len(music)):
        if music[i] in notes.
            music_array.append(notes)
        notes[music[i])
    return music_array
#Test cases
test_music1 = 'o o| .| o| .| .| .| o o'
test_music2 = 'o o| .| o| o| .| .| .| o o o o'
test_music3 = 'o o o| .| o| .| .' o o'
test_music4 = 'another_music'

#Test function
def test_parse_music():
    assert parse_music(test_music1) == [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
    assert parse_music(test_music2) == [1, 1]
    assert parse_music(test_music3) == []
    assert parse_music(test_music4) == []
test_parse_music()
```