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
    # Test the function with empty list
    assert concatenate([]) == ''
    # Test the function with a list of one string
    assert concatenate(['a']) == 'a'
    # Test the function with a list of three strings
    assert concatenate(['a', 'b', 'c']) == 'abc'
    print("Test cases passed!")
```