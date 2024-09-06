```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(*strings)

# Tests
strings = ['a', 'b', 'c']
result = concatenate(strings)
assert result == 'abc'
strings = []
result = concatenate(strings)
assert result == ''
```

This code defines a function 'concatenate' that takes a list of strings as an argument and returns the concatenated string. The code also provides tests to verify the correctness of the 'concatenate' function.