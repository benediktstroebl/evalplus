```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        string
    """
    return ''.join(strings)
# Unit tests
def test_concatenate():
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([]) == ''
```
This code defines a `concatenate` function that takes a list of strings as an argument and concatenates them into a single string. It also has a test_concatenate function with tests that verify the correctness of the `concatenate` function.