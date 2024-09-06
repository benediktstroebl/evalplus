```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' '|')
    beats = []
    for note in notes:
        if note.startswith('o whole'):
            beats.append(4)
        elif note.startswith('half'):
            beats.append(2)
        elif note.startswith('quarter'):
            beats.append(1)
        else:
            raise ValueError("Invalid music string")

    return beats

# Example test cases
test_parse_music = []
test_parse_music.append("o .o|.")
test_parse_music.append("o notes:")
test_parse_music.append("o whole:")
test_parse_music.append("quarter:")
test_parse_music.append("notes:")
test_parse_music.append("whole:")
test_parse_music.append("half:")
test_parse_music.append("quarter:")

test_parse_music.append("invalid:")
test_parse_music.append("notes:")
test_parse_music.append("invalid:")

def test_functions():
    assert parse_music("o o| .| o| o| .| .| .| .| o o") == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music(".") == []
    assert parse_music("four") == [4]
    assert parse_music("o o| .o|.") == [2, 2]
    assert parse_music("whole ") == []
    assert parse_music("half ") == []
    assert parse_music("quarter ") == []
    assert parse_music(".") == []
    assert parse_music("quarter o") == [1]
    assert parse_music("half o") == []
``` 
The provided Python script defines a function parse_music that takes a music_string as input and returns a list of integers representing the number of beats for each note. The music_string is parsed by splitting it into individual notes separated by '|'. The function then iterates through the notes, checking if it's a whole note ('o'), a half note, or a quarter note. If the note is a whole note, it adds 4 beats; if it's a half note, it adds 2 beats; if it's a quarter note, it adds 1 beat. If the note doesn't match any of these, a ValueError is raised.

The script also includes a set of test cases to validate the function. These tests demonstrate the most expected behavior of the parse_music function and can be used to ensure that the function is working correctly.