```python
from typing import List
def longest(strings: List[str]): 
    """ Returns the length of the longest string.
    >>> longest(['a'])
    [[Any valid string will do] 
    """
    if not strings: 
        return None
    return max(strings, key=len)

# Testing the function
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Output: 3
```