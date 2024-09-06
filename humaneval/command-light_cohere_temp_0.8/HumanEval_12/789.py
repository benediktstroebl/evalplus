```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Out of list of strings, return the longest one.
    >>> return max(strings, key=len)
    """
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'c'

strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = []
print(longest(strings))  # Output: None

strings = ['aa', 'bb', 'ccc']
print(longest(['aa', 'bb', 'ccc']))  # Output: 'aa'
```