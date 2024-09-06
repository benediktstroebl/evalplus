```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = {'o' : 4, 'o|' : 2, '.' : 1}
    notes_of_beats = [notes[ch] for ch in music_string.replace(notes)]
    print(notes_of_beats)
    return notes_of_beats
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    beats_expected = parse_music(music_str)
    print(beats_expected)
    for beat in beats_expected:
        if beat != 4:
            print("Error: Expected 4 beats, got", beat)
            return False
    return True
```