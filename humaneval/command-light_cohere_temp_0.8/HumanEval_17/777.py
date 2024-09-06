Here is a Python script that includes the self-contained function `parse_music` that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format.
    It task is legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Returns:
    A list of integers corresponding to how many beats each note lasted.
    """
string has to match this exact pattern. 
"""
    # Regex to match pattern in music_string
    regex = r'(o|o\urst|.) |.')*([oO])'

    # Parse and return list of beats
    beats = regex.findall(regex, music_string)[0]

    return beats

# Unit tests
def test_parse_music():
    music_string = 'oo oO|oo oO|oo .o O| oO|oo oO .o O|oo .o o'
    assert parse_music(music_string) == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]

test_parse_music()
```

This script defines a function `parse_music` that parses a music_string according to the given pattern and returns a list of integers that represent the number of beats each note lasted. The function also includes a unit test `test_parse_music` that checks if the `parse_music` function is working correctly for a given input string.