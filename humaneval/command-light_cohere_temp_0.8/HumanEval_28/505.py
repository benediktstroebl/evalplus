Here's a self-contained Python script with a function that concatenates lists of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    # Test the function with an empty list
    assert concatenate([]) == ''
    # Test the function with a list of one string
    assert concatenate(['a']) == 'a'
    # Test the function with a list of three strings
    assert concatenate(['a', 'b', 'c']) == 'abc'
    # Test the function with a list of mixed strings
    assert concatenate(['a', 'bc', 'd']) == 'abcd'
    return
test_concatenate()
```
This script provides a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string. The `test_concatenate` function contains several test cases to validate the correctness of the `concatenate` function.