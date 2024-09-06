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
    # Test the function with a list of strings
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The function concatenate takes a list of strings as input and returns the concatenated string. The function uses the own list comprehension to create the concatenated string. The test_concatenate function tests the function by asserting that it returns the expected result for the given input.

Remember, when you run this script, it will provide all the tests passed successfully.