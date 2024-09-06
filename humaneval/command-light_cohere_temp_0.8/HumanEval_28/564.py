```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        string
    """
    return ''.join(strings)

# Test the function
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```

This script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The `test_concatenate` function is used to test the correctness of the `concatenate` function with various inputs.