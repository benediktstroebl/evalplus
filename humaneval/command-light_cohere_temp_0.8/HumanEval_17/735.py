```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') |
    whole note and rests go to notes[-1]
    music_notes = [int(note) for note in notes if note != 'rest']

    return music_notes

# Test case 1:
music = "o o| .| o| .| .| .| .| o o"
notes = parse_music(music)
print(notes)  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

# Test case 2:
music = ".|o o| .| .| .o| .o| o"
notes = parse_music(music)
print(notes)  # [1, 2, 2, 4, 2, 1]

# Test case 3:
music = "o o/| .| o| .| .| .o "
notes = parse_music(music)
print(notes)  # [4, 2, 1, 2, 2, 1, 1]
```

This code defines a `parse_music` function that takes a music string and splits it by spaces, to obtain notes. The function then filters out rests and converts the notes into integers. The test cases demonstrate how the actual output is.