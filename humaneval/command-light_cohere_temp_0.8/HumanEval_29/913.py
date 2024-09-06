```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    Returns a Filter the a list of strings, and returns a new list containing only the strings that start with the specified prefix.
    >>> ['abc', 'bcd', 'cde', 'array', 'for']
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```