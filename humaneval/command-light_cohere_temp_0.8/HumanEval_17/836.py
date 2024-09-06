```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    music = [notes[note] for note in music_string.parse()]
    would need function that can convert the input music_string into a list of integers.

def test_music_parser():
    # Test string 1
    music_str = 'o o| .| o| .| .| .| o o'
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]

    # Test string 2
    music_str = '..|.'
    assert parse_music(music_str) == [1]

    # Test string 3
    music_str = 'o o .'o.'
    assert parse_music(music_str) == [4, 1, 1, 4]

    # Test string 4
    music_str = 'o| o o'
    assert parse_music(music_str) == [1, 2, 2, 2]

    # Test string 5
    music_str = 'o o o|.'
    assert parse_music(music_str) == [4, 4, 1, 1]

    # Test string 6
    music_str = '.'* .o'
    assert parse_music(music_str) == [1, 4]

    # Test string 7
    music_str = 'o o o .o'
    assert parse_music(music_str) == [4, 4, 4, 1]

    # Test string 8
    music_str = 'o o o o|.'
    assert parse_music(music_str) == [4, 4, 4, 4]

test_music_parser()  # Test the function with all possible test cases
 ```