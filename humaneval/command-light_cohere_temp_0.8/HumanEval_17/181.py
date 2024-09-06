```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 1,
        "oo": 4,
        "oo|": 2,
        "oo."":": 1,
        "...": 4,
        "|.": 1,
        "..|": 1,
        "....": 4,
        "....|": 1
    }
    return [notes[char] for char in music_string.

# Test cases
def test_parse_music():
    assert parse_music("o o| .| o| .| .| .| .| o o") == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music(".") == [4]
    assert parse_music("...") == [4]
    assert parse_music("oo o| ") == [4, 2]
    assert parse_music("o o/ ") == [4, 2]
    assert parse_music(" o/o") == [4]
    assert parse_music(" o o| ") == [4, 2]
``` 
This Python script defines a function called `parse_music` that takes a music string as input and returns a list of integers. The function maps each characters in the music string to their respective beat values and then loops through these characters to build the list. 

The script also provides a set of test cases for the `parse_music` function to ensure its correctness.