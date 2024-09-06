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
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([['a'], ['b'], ['c']) == 'aabc'
```
The function `concatenate` in the script takes a list of strings and concatenates them into a single string. It uses the full name for the strings and returns the concatenated string. The `test_concatenate` function contains a series of tests, which check the correctness of the `concatenate` function using various input combinations.