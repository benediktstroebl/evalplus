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
def test_concatenate_empty_list():
    # Empty list should return empty string
    assert concatenate([]) == ''


def test_concatenate_non_empty_list():
    # Non-empty list should return concatenated string
    assert concatenate(['a', 'b', 'c']) == 'abc'
```

This script includes the `concatenate` function that takes a list of strings and returns a single string containing the concatenated elements. It also includes test functions to validate the function against two cases: an empty list input and a non-empty list input. You can use these tests to check correctness before running the function. 

To run the tests, you can add the following code before the `tests` block and execute the script:
```python
# If running directly, import the testing framework
from unittest import mock

# Run the tests
unittest.main()
``` 

This will run the tests and display the results, including any failures or errors.