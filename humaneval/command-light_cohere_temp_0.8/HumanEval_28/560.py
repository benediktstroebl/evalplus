```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of string
    Returns:
        string
    """
    return "".join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result) # Output: abc
strings = []
result = concatenate(strings)
print(result) # Output: ''
strings = ["".join"]
result = concatenate(strings)
print(result) # Output: 'a'
```