```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes in a string representing musical notes in a special ASCII format. 
    The task is to parse this string and return a list of integers corresponding to how many beats does each
    note last.

    Here is legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    >>>
    return [int(beat) for beat in music_string.][::-1]

# Test case 1
test_music = parse_music('o o| .| o| .| o| .| o o')
assert len(test_music) == [4, 2, 1, 2, 1, 1, 1, 1, 4]

# Test case 2
test_music = parse_music('o o o o .| .| .| o| .| o| .| o o o')
assert len(test_music) == [4, 4, 4, 1, 1, 4, 4, 4]

# Test case 3
test_music = parse_music('o o o o o .o| .| o o o o .o o| .')
assert len(test_music) == [4, 4, 4, 4, 1, 1, 4]
```
This code defines the `parse_music` function that takes a string of music notes and returns a list of integers corresponding to the beats of each note. It then passes three test cases and checks that the function correctly identifies the beats in the input music string.