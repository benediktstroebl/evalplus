```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Given music_string is a string representing notes in a special ASCII format.
    This task is parse the string and return list of integers corresponding to how many beats does each note last.
    Here's legend:
        - 'o' whole note, lasts 4 beats
        - 'o|' - half note, lasts 2 beats
        - '|' - quarter note, lasts 1 beat

    return [length for length in map(lambda x: int(x.split('|')[-1]), music_string.

# Test cases
# Test case 1
test_string = "o o| .| o| .| .| .| .| o o"
notes = parse_music(test_string)
print(notes)
# Test case 2
test_string = "o o o o| .| o| o .| .| .| o o o o"
notes = parse_music(test_string)
print(notes)
# Test case 3
test_string = "o o o o o o o o o o| . "o| o"
notes = parse_music(test_string)
print(notes)
```