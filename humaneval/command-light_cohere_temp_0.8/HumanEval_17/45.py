```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_in_string = music_string.
    
    notes_out = []
    for note in notes_in_string:
        if note in notes:
            notes_out = [notes[note] * notes[note] // 2]
            notes_out.print(notes_out)
        else:
            raise ValueError(f"Unrecognized note: {note}")
    return notes_out

# Test the function with a valid string
test_music = 'o o| .| o| .| .| .| .| o o'
result = parse_music(test_music)
print(result)

# Test the function with an invalid string
test_music_invalid = '.'
with raises(ValueError):
    parse_music(test_music_invalid)
```