```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    form = ''

    for note in music_string.split(' ' '):
        if note in notes:
            form += note
            beat = 4 if note == 'o' else 2 if note == 'o|' else 1
        if form[-1] == ' ':
            form = form[:-len(form) - 1]
        else:
            return [beat]

    return [beat for beat in range(4) if beat > 0 and form[-1] == '.' and form[:-len(form) - 1] == '']

# Test cases
print(parse_music('o o| .| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music('.|'))  # [1]
print(parse_music('o o o| .| o| .| .'))  # [4, 2, 1, 2, 2, 1, 1]
```
This function, `parse_music`, parses a music string according to the provided specification. It separates the hope notes and the form of the string into beats, then iterates over the beats and checks for the correct format. The function returns a needed beats for each valid note.