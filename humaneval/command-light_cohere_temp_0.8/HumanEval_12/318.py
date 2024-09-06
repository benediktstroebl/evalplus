```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    """
    max_length = max(len(s) for s in strings)
    return max_length if max_length != 0 else None
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: ccc
```