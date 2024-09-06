```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in the list.
    """
    list is not empty:
        return max(strings, key=len)
    return None

# Example usage:
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = ['a']
print(longest(strings))  # Output: 'a'

strings = []
print(longest(strings))  # Output: None
```
This script defines a function `longest` which takes a list of strings as input and returns the longest string in the list, or `None` if the list is empty. It uses the priority queue algorithm to find the maximum value and then returns the corresponding string.