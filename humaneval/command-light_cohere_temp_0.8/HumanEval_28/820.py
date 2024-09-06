```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: List of strings
    Returns:
    str: Concatented string
    """
    return "".join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: abc

strings = []
result = concatenate(strings)
print(result)  # Output: 

strings = ["a", "c"]
result = concatenate(strings)
print(result)  # Output: ac

strings = ["a", "b", "c"]
result = concatenate(strings[0] + strings[1] + strings[2])
print(result)  # Output: abc
```