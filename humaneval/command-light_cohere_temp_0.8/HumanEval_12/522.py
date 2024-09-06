```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the longest one.
    >>> longest(['a', 'b', 'c'])
    ['a']
    >>> longest(['a', 'bb', 'ccc'])
    ['ccc']
    >>> longest(['a', 'ab', 'aba'])
    ['aba']
    """
    if not strings:
        return None
    max_length = max(len(string) for string in strings)
    return strings[max_length]
```