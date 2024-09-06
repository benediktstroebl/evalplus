```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return "".join(*strings)
def test_concatenate():
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'abcA'
    assert concatenate(['abc', 'abc']) == 'abcabc'
```
This code defines the `concatenate` function, which takes a list of strings and returns their concatenation as a single string. The `test_concatenate` function contains a series of asserts that validate the correctness of the `concatenate` function.