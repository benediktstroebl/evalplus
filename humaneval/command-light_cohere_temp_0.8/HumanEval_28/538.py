```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        str: concatenated string
    """
    return ''.join(strings)
# Create test cases
test_cases = [
    [],  # Empty list
    ['a'],  # Single string
    ['a', 'b', 'c'],  # Two strings
    ['a', 'bc'],  # Only a with a space after it
]

# Test function
def test_concatenate():
    for test_case in test_cases:
        actual_concat = concatenate(test_case)
        expected = ''.join(test_case)
        assert actual_concat == expected, f"Failed for {test_case} expected {expected} but got {actual_concat}"
# Run the tests
test_concatenate()
 ``` 
This code defines a function `concatenate` that takes a list of strings and concatenates them into a single string. It also has a test cases with various strings, and the `concatenate` function is used to verify its correctness.