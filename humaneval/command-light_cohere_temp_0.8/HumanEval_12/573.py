```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    > Return the longest string from a list of strings.
    >>> Return the longest([])
    >>> 'a'
    >>> 'ccc'
    >>> ['a', 'bb', 'ccc']
    'ccc'
    >>> [x for x in 'abcde']
    'de'
    >>> ['a', 'bb', 'ccc', 'abcde']
    'abcde'
    """
    if not strings:
        return None
    max_length = max(len(string) for string in strings)
    return strings[max_length - 1]
```