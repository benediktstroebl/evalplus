```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    # Test the function with empty list
    assert concatenate([]) == ''
    # Test the function with one string
    assert concatenate(['a']) == 'a'
    # Test the function with two strings
    assert concatenate(['a', 'b']) == 'ab'
    # Test the function with more than two strings
    assert concatenate(['a', 'b', 'c']) == 'abc'
if __name__ == '__main__':
    test_concatenate()
```
This script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The function is tested with various inputs to ensure its correctness.

The `test_concatenate` function contains tests to validate the `concatenate` function. 
When you run the script, it will run the tests and provide the results.