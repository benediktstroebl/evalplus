```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        string
    """
    return ''.join(strings)

# test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: abc

strings = []
result = concatenate(strings)
print(result)  # Output: 

strings = ["a", "bc"]
result = concatenate(strings)
print(result)  # Output: abc

strings = ["abc"]
result = concatenate(strings)
print(result)  # Output: abc
```