```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: List of strings to concatenate
    Returns:
    concatenated string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
```
This code defines a function called `concatenate` that takes in a list of strings as an argument and returns the concatenated string. The `test_concatenate` function contains a series of asserts that verify the correct behavior of the `concatenate` function. 

This code is self-contained and contains all the necessary logic and tests for the function.