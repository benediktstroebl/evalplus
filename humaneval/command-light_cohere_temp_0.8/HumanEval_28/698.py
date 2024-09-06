```python
from typing import List
def concatenate(strings: List[str]):
    """
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

def test_concatenate():
    """
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    assert concatenate([]) == '', "Function failed test 1"
    assert concatenate(['a', 'b', 'c']) == 'abc', "Function failed test 2"
```

The provided code defines a function `concatenate` that takes a list of strings and concatenates them into a single string. This function is two test to pass tests. The `test_concatenate` function is designed to verify the correctness of the `concatenate` function by passing in different inputs and asserting that the output is correct.