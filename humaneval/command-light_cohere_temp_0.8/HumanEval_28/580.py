```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# tests
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)
print(isinstance(result, str))
```