```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') '
    codes = []
    for note in notes:
        if note.startswith('o o'):
            codes.append(4)
        elif note.startswith('o o|'):
            codes.append(2)
        elif note.startswith('.|'):
            codes.append(1)
        else:
            codes.append(0)  # default for non-note characters

    return codes

# Test case 1
test_1 = parse_music('o o| .| o| .| .| .| o o')
test_1_result = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
assert test_1_result == parse_music(' '.join())

# Test case 2
test_2 = parse_music(' .| .o| o')
test_2_result = [2, 2]
assert test_2_result == parse_music('.o.')

# Test case 3
test_3 = parse_music(' .| .o| .o| .| .')
test_3_result = [1, 0, 0]
assert test_3_result == parse_music('. ')
```
This function parse_music takes a string music_string as input and returns a list of integers. The function splits the strings in the music_string into separate notes, and then extracts the length of each note by looking at its first character. The code then uses theas a simple set of rules to determine the length of each note.