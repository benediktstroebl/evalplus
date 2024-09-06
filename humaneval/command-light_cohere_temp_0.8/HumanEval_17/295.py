```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('o public ')
    notes
    notes = [int(note) for note in notes if note.isalpha()]
    done
    if len(notes) != 6:
        raise ValueError('Not 6 notes found in music string!')
    return notes

# test cases for this function
def test_music():
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o o| o| .| .| .| .| .| o o') == [4, 4, 1, 1, 1, 4, 4]
    assert parse_music('.") == []
    assert parse_music('x') == []
    assert parse_music('oo') == []
```
This Python code defines a function `parse_music` that parses a music string containing musical notes. The function splits the the string into a list of notes, which are then converted into integers. The function also includes several test cases to verify its functionality, such as checking if it correctly handles different inputs. 

This self-contained solution demonstrates the logic for parsing musical notes in a string.