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
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate([123]) == '123'
    assert concatenate([123, 45]) == '123645'
    assert concatenate(['a', 'bc', 'd']) == 'abc'd'
```
This Python code defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string. The function uses the also includes a test function `test_concatenate` that contains a number of tests for the `concatenate` function, which ensures that the function is working correctly.