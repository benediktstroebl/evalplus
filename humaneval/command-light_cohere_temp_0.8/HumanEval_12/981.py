```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    Returns the first one in case of length-tie.
    >>> longest(['a', 'b'])
    'a'
    >>> longest(['a', 'bb'])
    'bb'
    >>> longest(['aa', 'bb', 'ccc'])
    'bb'
    """
    if not strings:
        return None
    max_len = max([len(x) for x in strings])
    return strings[max_len - 1]
```