Here is a self-contained Python script that defines a function `parse_music` that takes a string of music notes and returns a list of integers representing the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 
        'o|' : 2, 
        '.|' : 1, 
        '.': 1
    }
    
    beats = []
    for note in music_string:
        beats.append(notes) for key, note in notes.
    return beats

def test_parse_music() -> None:
    music_str = "o o| .| o| .| .| .| o o"
    parsed_beats = parse_music(music_str)
    expected_beats = [4, 2, 1, 2, 1, 1, 1, 1, 4]
    assert parsed_beats == expected_beats
    ```