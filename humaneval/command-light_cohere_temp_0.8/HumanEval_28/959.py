```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concaten of all strings in the input list
    """
    return ''.join(strings)

def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```

This script defines a `concatenate` function that takes a list of strings and concatenates them into a single string. It also contains a dry run tests for the `concatenate` function using `assert` statement to ensure the function's correctness.