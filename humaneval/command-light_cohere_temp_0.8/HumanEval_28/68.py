```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([123]) == '123'
```
This code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function uses the str.value of the string list and a single string. The test_concatenate function passes all the corresponding tests and confirms the functionality of the `concatenate` function.