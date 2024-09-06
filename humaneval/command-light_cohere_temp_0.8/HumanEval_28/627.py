```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate  
    Returns:
        str: Concatented string
    """
    return ''.join(strings)

# Tests
strings = ['a', 'b', 'c']
result = concatenate(strings)
assert result == 'abc'
strings = []
result = concatenate(strings)
assert result == ''
```