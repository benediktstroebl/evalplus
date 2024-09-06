```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', ' ', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', ' ', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
This script defines a `concatenate` function that takes a list of strings and returns their concatenation as a single string. It also has a test function that checks the correctness of the `concatenate` function for different inputs.