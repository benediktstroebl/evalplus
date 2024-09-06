```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: List of strings to concatenate
    Returns:
        Concatenated string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([
        '123',
        'abc'
    ]) == '123abc'
```
The `concatenate` function takes a list of strings as input and returns the concatenated string. The `test_concatenate` function provides a series of test cases to verify the correctness of the `concatenate` function.