```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
   >>> Returns: List[str]
    >>> strings = ['abc', 'bcd', 'cde', 'array', 'hello']
    >>> filter_by_prefix(strings, 'a')
    ['abc', 'array']
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'hello'], 'x')
    []
    """
    return [string for string in strings if string.startswith(prefix)]
```