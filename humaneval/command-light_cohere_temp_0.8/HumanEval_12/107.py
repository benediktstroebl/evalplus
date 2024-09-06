```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list.
    Parameters:
        strings (List[str]): list of strings
    Returns:
        str: longest string in the list
    """
    return max(strings, key=len)

# Unit tests
def test_longest():
    assert longest(['a', 'bb', 'ccc']) == 'ccc'

test_longest()
```
This script defines a Python function `longest` that takes a list of strings and returns the longest string in the list. It uses the maximum function with the `key=len` to identify the longest string. 

The function is then tested with a sample input using the `test_longest` function, which asserts that the result of the `longest` function is correct for the given input.