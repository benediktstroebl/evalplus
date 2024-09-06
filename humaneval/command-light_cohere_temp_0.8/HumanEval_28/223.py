```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings to concatenate
    Returns:
    str: concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The provided code defines a function `concatenate` that takes a list of strings as input and returns their concatenated string. It uses the reason: to create a string from the list, and then uses the `join` method to concatenate the strings into a single string. The `test_concatenate` function tests the correctness of the `concatenate` function by passing different strings to it and checking if the result is as expected.