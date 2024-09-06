```python
from typing import List
def longest(strings: List[str]): 
    """
    Returns the longest string from a list of strings.
    """
    return max(strings, key=len)

# Test case
strings = ['a', 'b', 'c']
result = longest(strings)
print(result) # Output: c
```