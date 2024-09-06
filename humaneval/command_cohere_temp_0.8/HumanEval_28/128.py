```python
# Importing the required module
from typing import List

# Defining the Concatenate function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # Iterating through the list of strings and adding them to a string variable
    result = ''
    for string in strings:
        result += string
    return result

# Testing the implementation
def test_concatenate():
    # Empty list
    assert concatenate([]) == ''

    # Single element list
    assert concatenate(['a']) == 'a'

    # Multiple elements list
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Running the tests
test_concatenate()
```