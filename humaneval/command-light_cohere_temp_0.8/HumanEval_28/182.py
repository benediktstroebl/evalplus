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
strings = []
print(concatenate(strings))  # Output: ''
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
strings = ['1', '2', '3']
print(concatenate(strings))  # Output: '123'
```