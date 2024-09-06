```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string in the list.
    >>> longest(['a', 'bc', 'abc'])
    'abc'
    """
    return max(map(len,strings))
```