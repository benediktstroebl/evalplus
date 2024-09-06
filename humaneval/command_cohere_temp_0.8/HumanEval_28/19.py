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
    # Test case 1: Empty list
    assert concatenate([]) == ''


def test_concatenate_non_empty_list():
    # Test case 2: List with elements
    assert concatenate(['a', 'b', 'c']) == 'abc'


# Run the tests
test_concatenate_empty_list()
test_concatenate_non_empty_list()
```