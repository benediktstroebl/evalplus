```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')
    high='o o| o|.' note
    result = [len(note) for note in high. ][::-1]
    return result

def test_parse_music():
    test_str = 'o o| .| o| o| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(test_str)
    assert actual == expected, f"expected {expected}, but got {actual}"

# Run the test function to check the solution
test_parse_music()
 ```