```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the longest string from the list.
    >>> longest(['a', 'bb', 'ccc'])
    ['ccc']
    """
    return max(strings, key=len)
```