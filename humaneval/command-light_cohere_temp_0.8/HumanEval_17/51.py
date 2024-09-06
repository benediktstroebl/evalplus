Here's the code:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')
    music_notes = []
    for note in notes:
        note = note.split(' ')
        note_chars = note.split(' ')
        note_ints = []
        for i, char in enumerate(note_chars):
            if char == 'o':
                note_ints = [4]
            elif char == 'o|':
                note_ints = [2]
            elif char == '.|':
                note_ints.append(1)
        note_ints.append(4)
        note_ints.append(2)
        music_notes.append(note_ints)
    return music_notes

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(music_str)
    assert actual == expected
```

This code defines a function `parse_music` that takes a music string in markdown code format as input and returns a list of integers that correspond to the number of beats for each note in the music. It uses the legend to specify the beats of each note. The test case section at the `test_parse_music` verifies that the `parse_music` function produces the correct output for a given input.