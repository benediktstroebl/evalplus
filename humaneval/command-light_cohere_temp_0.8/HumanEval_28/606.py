```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        str: concatenated string
    """
    return "".join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([None, 'a']) == 'a'
    assert concatenate(['a', 'ab']) == 'abab'
```
The provided code defines a function `concatenate` that takes a list of strings as input and returns their concatenation as a single string. The `test_concatenate` function contains a series of asserts that verify the correctness of the `concatenate` function with various input strings.