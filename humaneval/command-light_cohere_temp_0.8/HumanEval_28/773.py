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

# Test cases
strings = ['a', 'b', 'c']
result = concatenate(strings)
assert result == 'abc'
strings = []
result = concatenate(strings)
assert result == ''
```
This script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It is using the string formatting and tuple unpacking to make the docstring more readable. The test cases demonstrate the good usage of the `concatenate` function.