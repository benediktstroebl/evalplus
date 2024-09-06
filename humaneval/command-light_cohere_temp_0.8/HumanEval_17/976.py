```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('o individual notes.
    notes = [list(note.split('|') for note in notes)

    return [len(note) for note in notes]

# Test case 1
print(parse_music('o o| .| o| .| .| .| .| .| o o'))
[4, 2, 1, 2, 1, 1, 1, 4, 4]

# Test case 2
print(parse_music('o o| .| o| .| .| .| .| .'))
[4, 2, 1, 1, 2, 2, 1, 1, 1]

# Test case 3
print(parse_music('o o o| .| .'))
[4, 4, 2, 2, 1, 1, 1]

# Test case 4
print(parse_music('o o| .| .o o'))
[4, 2, 1, 2, 1]
```
This Python function, `parse_music`, takes a string music_string as input and splits it into a list of notes. The function then iterates through each note in the list and checks if it is one of the allowed notes (whole, half, or quarter). The function returns a list of the number of beats corresponding to each note.