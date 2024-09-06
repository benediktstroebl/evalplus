```python
from typing import List
def concatenate(strings: List[str]):
    """
    Concatenate list of strings into a single string and return.
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# Test the function with sample inputs
strings = ['a', 'b', 'c']
result = concatenate(strings)
assert result == 'abc'
strings = ['a', '#', '1234']
result = concatenate(strings)
assert result == '#1234'
```