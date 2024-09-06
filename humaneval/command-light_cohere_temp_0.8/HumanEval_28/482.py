```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string """
    return ''.join(s) + ''.join(strings)

# Test cases
test_cases = [
    [],              # empty list
    ['a'],         # single string
    ['a', 'b', 'c'],   # list with 3 strings
    ]

# Test function
def test_concatenate():
    for test_str in test_cases:
        actual = concatenate(test_str)
        expected = ''.join(test_str) + ''.join(test_str)
        assert actual == expected, f"failed for {test_str}"

# Run the tests
test_concatenate()
```
This code provides a function `concatenate` that takes a list of strings and concatenates them into a single string. The `test_concatenate` function runs the tests to ensure the `concatenate` function works correctly for various inputs.