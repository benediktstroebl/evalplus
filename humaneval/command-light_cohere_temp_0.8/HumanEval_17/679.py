```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')').
    notes = [int(note) for note in notes if note.split('o
    needed to be in [".pad', 'o', 'o|', '|', '.')]
    return [len(note) for note in notes if note[0] == 'o']

# Test case
music1 = 'o o| .| o| .| .| .| .| o o'
test_parse_music(music1)

# Test case 2
music2 = '.'
test_parse_music(music2)
```

This Python script defines a function `parse_music` that takes a music string in the format of musical notes. The function splits the notes by whitespaces and then extracts the integer representation of the notes. The function returns a list of the lengths of whole notes.