```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: List of strings
    Returns:
        str: Concatented string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
``` 
The provided Python code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The `test_concatenate` function contains several assertions that verify the correctness of the `concatenate` function by testing different input cases.

This code provides a self-contained way to solve the problem of string concatenation and passes all tests.