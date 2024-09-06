```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[char] for char in music_string.inject + '\n +']
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    parsed_notes = parse_music(music_str)
    assert parsed_notes == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4] == [int(note) for note in music_str.test_parse_music()
```

This Python script defines a function `parse_music` that takes a string of music notes in a specific format and returns a list of integers, representing the duration of each note in the music. The function uses a dictionary to map musical notes to their durations, and then iterates over each character in the input string, looking up the note in the dictionary to find its duration and adding it to the result. The `test_parse_music` function tests the `parse_music` function by creating a test music string and asserting that the returned list of integers is correct.