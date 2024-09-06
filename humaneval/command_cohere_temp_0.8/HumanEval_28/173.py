```python
# Importing the necessary module
from typing import List


# Define the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result


# Provide tests
def test_concatenate():
    """
    Tests for the concatenate function.
    """

    # Case 1: Empty list
    assert concatenate([]) == ''

    # Case 2: List of strings
    assert concatenate(['a', 'b', 'c']) == 'abc'

    # Case 3: List with different types
    try:
        concatenate([1, 2, 'abc'])
    except TypeError as e:
        assert str(e) == 'All elements in the list must be strings'


# Run the tests
test_concatenate()
```

This script includes the `concatenate` function and a test suite, which verifies that the function behaves as expected. The `test_concatenate` function includes multiple test cases to validate the functionality of the `concatenate` function. It checks for an empty list, a list of strings, and a list with different types to ensure robustness in different scenarios.