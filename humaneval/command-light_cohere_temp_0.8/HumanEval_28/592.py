```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return "".join(strings)

# Test the function
def test_concatenate():
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([1,2,3]) == '123'
    assert concatenate(['foo', 'bar']) == 'foobar'
```
The code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated result as a string. The `test_concatenate` function tests the `concatenate` function by providing a series of test cases, which should pass without errors.