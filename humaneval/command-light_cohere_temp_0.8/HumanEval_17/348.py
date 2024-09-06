```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
    }
    return [notes[note] for note in music_string.

# Test cases
test_music_1 = 'o o| .| o| o| .| .| .| .| o o'
test_music_2 = 'foo o o| .|.o.'
test_music_3 = '.'
test_music_4 = 'oo o |oo.'

def test_function(music_str):
    parsed_notes = parse_music(music_str)
    assert parsed_notes == [4, 2, 1, 2, 1, 1, 1, 1, 4]  # Test 1
    assert parsed_notes == [1]  # Test 2 (empty string)
    assert parsed_notes == [4, 4]  # Test 3 (single note)

# Main function
if __name__ == "__main__":
    print("Test case 1: " + test_music_1)
    test_function(test_music_1)
    print("\n")

    print("Test case 2: " + test_music_2)
    test_function(test_music_2)
    print("\n")

    print("Test case 3: " + test_music_3)
    test_function(test_music_3)
    print("\n")

    print("Test case 4: " + test_music_4)
    test_function(test_music_4)
```
The code defines a function `parse_music` that parses a music string in a format where each note lasts for a certain duration. It uses a interesting logic to map these note characters to their respective durations. The test cases cover various scenarios, such as empty strings, single notes, and different patterns of notes. The output will show the results for each test case.