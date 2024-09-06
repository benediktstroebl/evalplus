```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' '|')
    notes = [int(x) for x in notes]
    return notes

# Test cases
tests = [
    'parse_music("o o| .| o| .| .| .| o o")
    [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
    # ... add more test cases ...

# Check if all functions return the correct results
for test in tests:
    actual = parse_music(test)
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
    if actual != expected:
        print(f"Test {test} failed.")
    else:
        print(f"Test {test} passed.")
``` 
This code defines a function `parse_music` that takes a string of music notes separated by `|`, splits it into a list of integers, and then returns that list. The test cases ensure that the function works correctly.