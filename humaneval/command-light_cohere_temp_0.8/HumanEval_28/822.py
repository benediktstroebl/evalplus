```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'acb'
    assert concatenate([]) == ''  # empty list should return empty string
test_concatenate()
```
This code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It also provides a test cases to test the correctness of the `concatenate` function. 

Note: The `test_concatenate` function is used to check if the concatenate function is working correctly for various inputs.