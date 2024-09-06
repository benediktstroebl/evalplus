```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Return list of integers corresponding to how many beats does each note last.
    """

    string is parsed into a list of integers representing the beats for each note.

test_music_parser = """
'o o| .| o| .| .| .| .| .| o o'
"""
result = parse_music(test_music_parser)
assert len(result) == 12
result = parse_music('')
assert len(result) == 0
result = parse_music('oo oo o| .| o| .| .')
assert len(result) == 7
result = parse_music('oo o o| .| .o .')
assert len(result) == 1
result = parse_music('o o| o| .| .| .')
assert len(result) == 3

print(result)
```