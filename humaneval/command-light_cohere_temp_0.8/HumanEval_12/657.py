```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, returns the longest one.
    """
    return max(strings, key=len)
    """
    return max(strings, key=len)

# Example usage
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'c'

strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = []
print(longest(strings))  # Output: None
```
The provided Python script defines a function `longest()` that takes a list of strings as input and returns the length of the longest string in the list. The `max()` function is then used to find the longest string, and the `len` function is used as the key to sort the strings by length.