```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: List of strings to concatenate
    Returns:
    concatenated string
    """
    return ''.join(*strings)

# Test cases
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result) # Output: abc
strings = []
result = concatenate(strings)
print(result) # Output: 

strings = ['a', '123', '456']
result = concatenate(strings)
print(result) # Output: 123456
```