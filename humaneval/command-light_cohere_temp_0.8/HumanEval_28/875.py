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
    """
    Test the concatenate function
    Args:
    """
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([3]) == '003'
    assert concatenate(['aa', 'a']) == 'aaa'
```
The function `concatenate` takes a list of strings as input and returns the concatenated string. The test function uses several input cases to test the correctness of the `concatenate` function.