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
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The code defines a `concatenate` function that takes a list of strings as an argument and returns the concatenated string. The `test_concatenate` function contains several test cases to ensure the correctness of the `concatenate` function.