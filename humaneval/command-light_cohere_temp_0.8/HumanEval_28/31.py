```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concaten result
    """
    return ''.join(*strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The code defines the `concatenate` function that takes a list of strings as input and returns the concatenated result as a single string. The function uses the in Python `*` operator to concatenate all elements in the input list. This code also provides a test function to verify the correctness of the `concatenate` function by passing the test cases.