```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Returns: str - concatenated string
    """
    return ''.join(strings)

# Test the function
def test_concatenate():
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate(['']) == ''
    assert concatenate(['a', '', 'b']) == 'ab'
    assert concatenate(['a', '']) == 'a'
    assert concatenate([1, 2, 3]) == '123'
    assert concatenate(['a', 'bb', 'ccc']) == 'aabbccc'
```
This script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. It also includes a test cases to validate the function. 

The `test_concatenate` function tests the `concatenate` function with a variety of input scenarios.