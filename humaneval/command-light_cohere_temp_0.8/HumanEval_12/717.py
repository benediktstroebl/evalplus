```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from the list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest([])
    None
    >>> longest(['aa', 'a'])
    'aa'
    """
    if not strings:
        return None
    max_len = max(len(string) for string in strings)
    return strings[max_len]
```