```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings
    Returns:
    string
    """
    return ''.join(strings)

# Test the function
strings = ['a', 'bc', '']
result = concatenate(strings)
assert result == 'abc'

# Test the function with empty list
strings = []
result = concatenate(strings)
assert result == ''
```
This code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. It then passes the Read tests to verify its correctness, including an empty list test. The output will be the specific values.