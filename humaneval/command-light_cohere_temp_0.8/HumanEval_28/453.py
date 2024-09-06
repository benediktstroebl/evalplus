```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join("".join(strings) )

def test_concatenate():
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```

This Python code defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string. The `test_concatenate` function tests the `concatenate` function by providing test cases that should return the expected results.