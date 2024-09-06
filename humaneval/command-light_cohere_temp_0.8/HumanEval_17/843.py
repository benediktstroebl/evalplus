```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    result = [notes[note] for note in music_string.or
    string_to_notes = str(music_string). Write a list comprehension to convert this string into a list of characters.
    return [list(string_to_notes)

def test_music():
    music_str = 'o o| .| o| .| .| .| o o'
    expected = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music(music_str) == expected
```