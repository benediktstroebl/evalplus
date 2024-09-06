```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string.
    >>> longest(['a', 'b', 'c']) == 3
    """
    return max(len(x) for x in strings)
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 3
```