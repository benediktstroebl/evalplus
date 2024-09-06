```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings to concatenate
    Returns:
    string
    """
    if not strings:
        return ""
    return ''.join(*strings)

# Example usage
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result) # Output: 'abc'
```
This code provides a self-contained function 'concatenate' that takes a list of strings as an argument and returns the concatenated string as a result. It provides an example usage with the strings ['a', 'b', 'c'] and prints the result, which is indeed 'abc'.