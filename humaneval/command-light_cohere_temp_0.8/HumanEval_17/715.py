```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') |
    whole_notes = []
    half_notes = []
    quarter_notes = []

    for note in music_string.split(' '.' crucial condition: '.'
    note = note.split(' ')

    each_note = [int(x) for x in note]
    notes.append(each_note[0])
    notes.append(each_note[1])
    notes.append(each_note[2])

    if len(notes) == 6:
        half_notes.append(notes[3])
        quarter_notes.append(notes[4])

    return [len(notes), len(half_notes), len(quarter_notes)]

# Test cases
def test_parse_music():
    music_string = 'o o| .| o| .| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music(music_string) == expected

    music_string = 'o o| | .| o| .| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music(music_string) == expected

    music_string = 'o o o o| .' .| o| .| .| .'
    expected = [4, 4, 4, 4]
    assert parse_music(music_string) == expected

    music_string = '.' * 'o o o o o o o o o o o o o'
    expected = [0, 0, 0, 0]
    assert parse_music(music_string) == expected

    music_string = 'o o o o| . .' .' o o o o o o o o o o'
    expected = [4, 4, 4, 4]
    assert parse_music(music_string) == expected

    music_string = 'o o o o o o o| .| .o .o .o'
    expected = [4, 4, 4, 4]
    assert parse_music(music_string) == expected

    music_string = '.' * 'o o o o o o o o .' .o'
    expected = [0, 0, 0, 0]
    assert parse_music(music_string) == expected

    music_string = 'oo|oo|.    .o.'
    with pytest.raises(ValueError): assert parse_music(music_string)

In this script, we have a function `parse_music` that takes a music string as input and returns a list of integers representing the number of beats in each note. We then test this string and make sure the parse function passes all corresponding tests.