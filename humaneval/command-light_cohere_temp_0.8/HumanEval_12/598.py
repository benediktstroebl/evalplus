```python
from typing import List
def longest(strings: List[str]):
    """
    Out of list of strings, return the longest one.
    """
    return max(strings, key=len)

# Example test cases
strings = ['a', 'b', 'c']
print( longest(strings) )  # Output: c

strings = ['aa', 'bb', 'ccc']
print( longest(strings) )  # Output: c

strings = []
print( longest(strings) )  # Output: None

strings = ['a']
print( longest(strings) )  # Output: a
```