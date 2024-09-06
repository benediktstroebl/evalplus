```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    symbol = ''
    beat = 4
    note_values = []

    for char in music_string:
        if char == ' ':
            symbol = ''
        elif symbol == '':
            note = notes[char]
            beat -= 1
            note_values.append(beat)
            symbol = char
        elif symbol == '|':
            if note_values:
                note_values.append(beat)
            symbol = ''
            beat = 4
            note_values = []

    return note_values

# Testing function
def test_parse_music(test_str: str):
    music_string = 'o o| .| o| .| .| .| .| o o'
    notes = parse_music(music_string)

    print(notes)
```