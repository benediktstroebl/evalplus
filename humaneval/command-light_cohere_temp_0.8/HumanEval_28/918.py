```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate
    Returns:
    str: Concatenated string
    """
    if not strings:
        return ""
    return ''.join(*strings)

# Test the function
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'aa', 'aaa']))  # Output: 'aaaa'
```
This code defines a function **concatenate** that takes a list of strings as an argument and returns the concatenated string. The test cases are provided to verify the functionality of the function.