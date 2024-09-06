```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.from lower() in notes]

def test_music_parser():
    music_str = 'o o| .| o| .| .| .| .| o o'
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

# Run the function and test
if __name__ == "__main__":
    test_music_parser()
``` 
This code defines a function called `parse_music` that takes a string of music notes, then maps those notes to the appropriate number of beats. The `test_music_parser` function is a simple test driver that creates a string of music notes, and passes it to the `parse_music` function. 
This code uses the typing module to make the function parameter `music_string` a string, and the function output `notes` a list of integers.