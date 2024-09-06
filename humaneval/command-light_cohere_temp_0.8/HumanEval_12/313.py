```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the length of the longest string in the list.
    >>> longest(['a', 'bb', 'ccc'])
    ['ccc', 'a']
    """
    return max(len(x) for x in strings)
```