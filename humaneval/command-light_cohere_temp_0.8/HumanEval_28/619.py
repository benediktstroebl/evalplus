```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        str: concatenated string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
```
The function concatenate takes a list of strings as input and returns the concatenated string. The function then follows the tested with a series of simple cases, and the test_concatenate function verifies the correctness of the concatenate function by passing in various lists of strings and asserting that the output is as expected.