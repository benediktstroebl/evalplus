```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings to concatenate
    Returns:
        concatenated string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([None]) == ''
```
The provided code defines a Python script with a self-contained function `concatenate` that concatenates a list of strings into a single string. The `test_concatenate` function contains several assertions that validate the correctness of the `concatenate` function.