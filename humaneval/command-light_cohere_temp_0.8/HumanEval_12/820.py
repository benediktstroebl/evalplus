```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return longest(['a', 'bb', 'ccc']) # Output: 'ccc'
    >>> longest([]) # Output: None
    >>> longest(['a', 'aa', 'aaa']) # Output: 'aaa'
    >>> longest(['aa', 'a', 'a']) # Output: 'aa'
    >>> longest(['aa', 'bb', 'a']) # Output: 'aa'
    >>> longest(['a', 'ab', 'abc']) # Output: 'abc'
    """
    if not strings:
        return None
    max_length = max(len(string) for string in strings)
    return strings[max_length]
```