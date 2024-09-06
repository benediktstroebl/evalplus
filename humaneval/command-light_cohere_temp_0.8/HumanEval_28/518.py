```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(''.join(strings) if strings else '')

def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```

This code defines a `concatenate` function that takes a list of strings and concatenates them into a single string. It also comes a dry running tests to verify the correctness of the `concatenate` function.