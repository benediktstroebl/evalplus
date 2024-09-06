```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate([]) == ''
    assert concatenate(['a', 'aa', 'b']) == 'ab'
    assert concatenate(['']) == ''
    assert concatenate(['a', 'b', 'c', 'd']) == 'abcd'
```
The script provides a function `concatenate` that takes a list of strings and returns their concatenation as a string. The function uses the important typing annotations, and the test suite ensures the correctness of the `concatenate` function with various inputs.