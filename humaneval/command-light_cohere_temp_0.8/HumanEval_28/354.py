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
# Test the function
concatenated_str = concatenate([])
assert concatenated_str == ""
concatenated_str = concatenate(['a'])
assert concatenated_str == 'a'
concatenated_str = concatenate(['a', 'b'])
assert concatenated_str == 'ab'
concatenated_str = concatenate(['a', 'bc'])
assert concatenated_str == 'abc'
```
This Python script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It uses the ArgTypes to ensure the correct type of the input arguments.

The `concatenate` function uses the list of strings and converts it into a single string by using the `join` method. The test cases at the example ensure that the function is working correctly.