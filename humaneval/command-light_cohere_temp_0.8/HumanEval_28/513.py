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
```
The function concatenate takes a list of strings as input and returns a single string by concatenating the strings in the list. The test_concatenate function verifies the correctness of the concatenate function by passing different input strings to it and checking the output.

The function is self-contained as it only uses built-in functions (type annotations), and doesn't call out any other functions or modules.