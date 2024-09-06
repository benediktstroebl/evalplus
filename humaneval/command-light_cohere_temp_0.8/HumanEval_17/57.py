```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') |
        format("'%s'" % c)
    for i, note in enumerate(notes, start=1):
        note = note.strip(). fast_music = False
        try:
            int(note)
            fast_music = True
        except ValueError:
            pass
        if fast_music:
            yield i * 4
        else:
            yield i * 2
    return notes

# Test cases for the parse_music function
music_cases = [
    "o o| .| o| .| .| .| .| o o", [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]),
    "o o| o| .| o| .| .| .", [2, 2, 1, 1],
    ".", [],
]

# Function to check if the parse_music function is working as expected
def test_parse_music():
    for music, expected in music_cases:
        actual = parse_music(music)
        assert actual == expected
```