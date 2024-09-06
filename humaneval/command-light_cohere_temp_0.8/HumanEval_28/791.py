```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: List of str, must not be empty
    Returns:
    str: Concatented string
    Raises:
    ValueError if strings is empty
    """
    if not strings:
        raise ValueError("Input list cannot be empty")
    return ''.join(strings)

# Unit tests
strings = ['a', 'b', 'c']
result = concatenate(strings)
assert result == 'abc'
strings = []
result = concatenate(strings)
assert result == ''
```