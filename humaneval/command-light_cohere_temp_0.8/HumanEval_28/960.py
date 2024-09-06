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
    """ Tests for the concatenate function
    """
    assert concatenate([]) == "", "Should return empty string"
    assert concatenate(['a']) == "a", "Should concatenate single string"
    assert concatenate(['a', 'b']) == "ab"
    assert concatenate(['a', 'b', 'c']) == "abc"
```
The provided code defines a function **concatenate** that takes a list of strings as input and returns the concatenated string. It also includes a test_concatenate, which contains a series of test cases that verify the correctness of the **concatenate** function.