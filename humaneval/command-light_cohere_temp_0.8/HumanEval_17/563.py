```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')
    split_reps are in the form 'o o|... o|...'. 
    music_notes = [int(note) for note in notes]
    return music_notes

# Test cases
test_cases = ['''
    'o o| .| o| .| .| .| .| o o'
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
    '''.split('\n')

# Run tests
if __name__ == "__main__":
    for test_case in test_cases:
        actual_notes = parse_music(test_case)
        expected_notes = [4, 2, 1, 2, 2, 1, 1, 1, 4]
        assert actual_notes == expected_notes, "Test case failed: " + test_case"
```
This code defines a function called `parse_music` that takes a string of music notes separated by spaces as input and returns a list of integers representing the number of beats for each note. The function splits the the string by space and then converts each note to an integer. The test cases ensure that the function is working correctly and that it returns the expected output for the given input.