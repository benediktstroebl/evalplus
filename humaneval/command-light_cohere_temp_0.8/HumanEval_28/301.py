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

def test_concatenate():
    assert concatenate([]) == '', 'No empty string'
    assert concatenate(['a']) == 'a', 'Expected single character'
    assert concatenate(['a', 'b']) == 'ab', 'Expected ab'
    assert concatenate(['a', 'bc']) == 'abc', 'Expected abc'
```
The provided code defines a `concatenate` function that takes a list of strings as an argument and concatenates them into a single string. The `test_concatenate` function contains tests to validate the `concatenate` function.