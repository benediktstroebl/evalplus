```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from the list.
    >>> strings = ['a', 'b', 'c']
    return max(strings, key=len)
    >>> strings = ['a', 'bb', 'ccc']
    return max(strings, key=len)
    >>> strings = ['aa', 'aa', 'a']
    return max(strings, key=len)
    >>> strings = ['ab', 'bb', 'ba', 'a', 'bb']
    return max(strings, key=len)
    >>> strings = ['a', 'bb', 'ccc', 'xx']
    return max(strings, key=len)
    """
    return max(strings, key=len)
```
Do you need help with anything else?