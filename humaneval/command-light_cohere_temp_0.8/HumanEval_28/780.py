```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate
    Returns:
    str: Concatenated string
    """
    return "".join(strings)

def test_concatenate():
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['ab', 'c']) == 'abc'
    assert concatenate(['abc', 'a']) == 'acba'
    assert concatenate([['a'], 'bc']) == 'abc'
    assert concatenate([['abc'], 'a']) == 'abcac'
    assert concatenate([1]) == '1'
```
This script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The `test_concatenate` function contains a series of assertions that verify the correctness of the `concatenate` function.