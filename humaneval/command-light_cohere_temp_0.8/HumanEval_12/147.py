```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Out of list of strings, returns the longest one
    """
    return max(strings, key=len)
# List of strings
strings = ['a', 'b', 'c']
# Test case 1
print(longest(strings))  # Output: 'a'

# Test case 2
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

# Test case 3
strings = []
print(longest(strings))  # Output: None
```