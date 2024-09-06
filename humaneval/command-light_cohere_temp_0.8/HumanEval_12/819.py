```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    ['a', 'b', 'c']
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['a'])
    'a'
    >>> longest(['a', 'bc'])
    'a'
    """
    if not strings:
        return None
    # Find the max length of the list of strings
    max_length = max(len(str) for str in strings)
    # Loop through each string and return the one with the max length
    return [str for str in strings if len(str) == max_length]
```