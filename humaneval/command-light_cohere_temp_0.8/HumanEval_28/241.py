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

# Unit tests
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
```
The provided Python script defines a function `concatenate` that takes a list of strings as input and returns the concatenated result as a single string. The function uses the optional chaining to concatenate the strings in the list using the `join` method, which makes the code more concise and readable.

The script also includes unit tests for the `concatenate` function using the `test_concatenate` function. The tests verify the strings empty list, a single string, and two strings being concatenated into a single string.