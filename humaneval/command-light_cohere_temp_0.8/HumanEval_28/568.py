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
    # Test empty list
    assert concatenate([]) == ''
    # Test single string
    assert concatenate('test') == 'test'
    # Test two strings
    assert concatenate(['test', ' Welcome']) == 'test Welcome'
    # Test more than two strings
    assert concatenate(['a', 'b', 'c', 'd', 'e']) == 'abcde'
    assert concatenate(['a', '!!!'] == 'a...')
    assert concatenate([{-1, 2, 3, 'four'}]) == '-23four'
```
This script provides a function `concatenate` that takes a list of strings and concatenates them into a single string. The `test_concatenate` function contains several test cases to ensure the correctness of the `concatenate` function.