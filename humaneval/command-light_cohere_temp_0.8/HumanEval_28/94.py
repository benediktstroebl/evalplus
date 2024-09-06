```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function uses the string ''.join() to create a string, and join the list of strings passed to the function using the join() method, which creates a single string by concatenating the strings in the list. The function is then passed to the `test_concatenate` function. The test then verifies that the expected behavior of the `concatenate` function.