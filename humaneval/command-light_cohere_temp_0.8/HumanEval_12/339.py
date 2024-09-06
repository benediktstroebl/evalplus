```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the longest string in a list of strings.
    >>> longest(['a', 'b', 'c']) == 'a'
    """
    return max(strings, key=len)
```