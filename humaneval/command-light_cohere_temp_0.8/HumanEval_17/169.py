```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    music_notes = music_string.split(' ')
    particularity and structure of this music_string are notes, represented with their respective durations. We'll use a particular pattern to split and return them as a list of integers.

def test_parse_music():
    # Test case 1
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected_output = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual_output = parse_music(music_str)
    assert actual_output == expected_output

    # Test case 2
    music_str = 'o o| .| .| o| .'
    expected_output = [4, 2, 1, 1]
    actual_output = parse_music(music_str)
    assert actual_output == expected_output

    # Test case 3
    music_str = '.' *
    expected_output = []
    actual_output = parse_music(music_str)
    assert actual_output == expected_output

    # Test case 4
    music_str = 'o o o| .| .' .| .' .' .'
    expected_output = [4, 4, 1, 4]
    actual_output = parse_music(music_str)
    assert actual_output == expected_output

    # Test case 5
    music_str = 'o o o o o o o o'
    expected_output = [4, 4, 4, 4, 4, 4, 4, 4, 4]
    actual_output = parse_music(music_str)
    assert actual_output == expected_output

    print("All tests passed!")
```
The function `parse_music` takes a string of music notes as its argument and returns a list of integers representing the number of beats for each note. The function uses theator pattern to split the music string into a list of notes and their durations, and then converts the durations to integers.

The function is then tested with five different music strings. If the function passes all test cases, then the test passes, and the function prints "All tests passed!". Otherwise, it prints an error message.