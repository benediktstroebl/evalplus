```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Out of list of strings, returns the length of the longest one.
    >>> longest(['a'])
    ['a']
    """
    return max(str(x).group(), key=len)[0] if strings else None
```