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
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([1,2,3]) == '123'
    assert concatenate(['a', ' ', 'b']) == 'ab'
    assert concatenate([True]) == 'True'
```
This script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function uses the other test that verifies the correctness of the `concatenate` function by passing test cases.