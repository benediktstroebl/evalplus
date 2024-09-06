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
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'acb'
    assert concatenate(['abc', 'abc']) == 'abcabc'
# run the test suite
test_concatenate()
```
This code provides a function `concatenate` that takes a list of strings as input and concatenates them into a single string. It also provides a dry tests for the function to ensure its correctness.