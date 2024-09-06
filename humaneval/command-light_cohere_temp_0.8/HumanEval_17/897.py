```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_in_use = []

    for note in music_string.split(' '.' commander |'):
        note = note.split(' ')
        notes_in_use.append(int(note) -4)
        return notes_in_use

# Test cases
test_parse_music = [
    "o o| .| o| .| .| .| .| o o",
    "  ",
    "  o",
    ".", ".|o",
    ".", ".o|.", ".o",
    " ",
    " o o o o",
    # invalid input, should return []
    "this is not valid music code",
]

for test in test_parse_music:
    actual_notes = parse_music(test)
    assert len(actual_notes) == 4 if 'o' in test else 2
    assert actual_notes == [4, 2, 1] if 'o' in test else actual_notes == []
```  This Python script defines a function **`parse_music`** that takes a music string as input and returns a list of integers. The function uses a legend to represent the duration of notes. It then loops through each character in the music string and appends the corresponding duration to a list named **`notes_in_use`**. Finally, the function returns this list. The script also includes a series of test cases to verify the correctness of the **`parse_music`** function.