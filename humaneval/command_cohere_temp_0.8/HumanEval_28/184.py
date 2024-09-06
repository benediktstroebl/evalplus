```python
# Importing the necessary module
from typing import List

# The function to be defined and solved
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result

# Unit tests
def test_concatenate_empty_list():
    """
    Test case for an empty list
    """
    assert concatenate([]) == ''

def test_concatenate_non_empty_list():
    """
    Test case for a non-empty list
    """
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Running the tests
test_concatenate_empty_list()
test_concatenate_non_empty_list()
```

This script includes the `concatenate` function and corresponding unit tests. The `test_concatenate_empty_list` function checks if the function correctly handles an empty list, resulting in an empty string. Meanwhile, `test_concatenate_non_empty_list` ensures that the function works as expected with a non-empty list, concatenating the strings as it should. Once executed, these tests verify the functionality of the `concatenate` function.