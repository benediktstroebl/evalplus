```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    
    Returns:
        str: Concatenated string
    """
    return "".join("".join(strings))
# Unit tests
def test_concatenate():
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The provided code defines a function called `concatenate` that takes a list of strings as an argument and returns the concatenated string. The `test_concatenate` function contains assertions that validate the correctness of the `concatenate` function by testing various input scenarios.