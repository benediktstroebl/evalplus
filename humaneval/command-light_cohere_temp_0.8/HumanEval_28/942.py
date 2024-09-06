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
# Add tests for the function
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'abcs'
    assert concatenate([1,2,3]) == '123'
```
The provided Python code defines a function `concatenate` that concatenates a list of strings into a single string. The `test_concatenate` function is used to add unit tests to the `concatenate` function.