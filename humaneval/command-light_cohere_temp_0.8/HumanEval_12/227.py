```python
from typing import List
def longest(strings: List[str]):
    """
    Return the length of the longest string.
    """
    return max(len(str), default=0)
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 3
```