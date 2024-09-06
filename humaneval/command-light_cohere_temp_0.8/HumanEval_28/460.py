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
    assert concatenate([123]) == '123'
```
The code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The function uses the different input/output tests to ensure its correctness. The `test_concatenate` function verifies the output of the `concatenate` function for various input strings.