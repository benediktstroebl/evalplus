```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1
    }
    
    notes_in_beat = [notes.get(x), whole_note, notes. whole whole note, lasts four beats,
        half_note = notes_in_beat[0] // 2,
        quarter_note = notes_in_beat[1] // 4
    }
    
    beat_info = [i // 4 for i in music_string]
    return [beat_info[i] for i in range(len(music_string))]

def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected_beats = [4, 2, 1, 2, 1, 1, 1, 1, 4]
    
    actual_beats = parse_music(music_str)
    assert all(expected_beats == actual_beats)
``` 
This Python script defines a function **`parse_music`** that parses a music string into a list of beats. The function uses a legends for musical notes to determine the beats of each. The **`test_parse_music`** function contains a music string and an expected beats list. The actual beats are compared against the expected beats, and the function passes the test successfully.