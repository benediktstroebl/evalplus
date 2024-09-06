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

# Example usage:
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
```
The `concatenate` function takes a list of strings as input and returns the concatenated string. It uses the native method `join `join` to convert the list of strings into a single string.