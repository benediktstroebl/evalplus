```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return "".join(strings)
def test_concatenate() -> None:
    """ Test the concatenate function
    Args: 
        nothing!
    Returns: 
        None
    """
    assert concatenate([]) == '', "Test 1 failed"
    assert concatenate(['a']) == 'a', "Test 2 failed"
    assert concatenate(['a', 'b', 'c']) == 'abc', "Test 3 failed"
    return None  # you can add additional tests as needed
```