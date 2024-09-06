```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: List of strings to concatenate
    :return: Concatenated string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    """
    Test the concatenate function
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    assert concatenate([]) == ''
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The `concatenate` function takes a list of strings as an argument and concatenates them into a single string. The `test_concatenate` function tests the `concatenate` function by passing various test cases, and asserts that the output of the function is correct.